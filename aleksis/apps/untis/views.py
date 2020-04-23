from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

from aleksis.core.decorators import admin_required
from aleksis.core.models import Group

from .filters import GroupFilter
from .forms import UntisUploadForm, GroupSubjectFormset, ChildGroupsForm
from .util.xml.xml import untis_import_xml


@login_required
@admin_required
def xml_import(request: HttpRequest) -> HttpResponse:
    context = {}

    upload_form = UntisUploadForm()

    if request.method == "POST":
        upload_form = UntisUploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            untis_import_xml(request, request.FILES["untis_xml"])

    context["upload_form"] = upload_form

    return render(request, "untis/xml_import.html", context)


# FIXME: Rule must check if setting is enabled
@admin_required
def groups_subjects(request: HttpRequest) -> HttpResponse:
    """ Assign subjects to groups (for matching by MySQL importer) """
    context = {}

    groups_qs = Group.objects.all()

    # Paginate
    paginator = Paginator(groups_qs, 100)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    groups_paged = groups_qs.filter(id__in=[g.id for g in page])

    # Create filtered queryset
    group_subject_formset = GroupSubjectFormset(
        request.POST or None, queryset=groups_paged
    )

    # Check if form is submitted and valid, then save
    if request.method == "POST":
        if group_subject_formset.is_valid():
            group_subject_formset.save()
            messages.success(request, _("Your changes were successfully saved."))

    context["formset"] = group_subject_formset
    context["page"] = page
    context["paginator"] = paginator

    return render(request, "untis/groups_subjects.html", context)


@admin_required
def groups_child_groups(request: HttpRequest) -> HttpResponse:
    """ Assign child groups to groups (for matching by MySQL importer) """
    context = {}

    # Apply filter
    filter = GroupFilter(request.GET, queryset=Group.objects.all())
    context["filter"] = filter

    # Paginate
    paginator = Paginator(filter.qs, 1)
    page_number = request.POST.get("page", request.POST.get("old_page"))

    if page_number:
        page = paginator.get_page(page_number)
        group = page[0]

        if "save" in request.POST:
            # Save
            form = ChildGroupsForm(request.POST)
            form.is_valid()

            if "child_groups" in form.cleaned_data:
                group.child_groups.set(form.cleaned_data["child_groups"])
                group.save()
                messages.success(request, _("The child groups were successfully saved."))
        else:
            # Init form
            form = ChildGroupsForm(initial={"child_groups": group.child_groups.all()})

        context["paginator"] = paginator
        context["page"] = page
        context["group"] = group
        context["form"] = form
    return render(request, "untis/groups_child_groups.html", context)
