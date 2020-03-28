from django.utils import timezone


def clean_array(a, conv=None):
    b = []
    for el in a:
        if el != '' and el != "0":
            if conv is not None:
                el = conv(el)
            b.append(el)
    return b


def untis_split_first(s, conv=None):
    return clean_array(s.split(","), conv=conv)


def untis_split_second(s, conv=None):
    return clean_array(s.split("~"), conv=conv)


def untis_split_third(s, conv=None):
    return clean_array(s.split(";"), conv=conv)


DATE_FORMAT = "%Y%m%d"


def untis_date_to_date(untis):
    return timezone.datetime.strptime(str(untis), DATE_FORMAT)


def date_to_untis_date(date):
    return date.strftime(DATE_FORMAT)


def untis_colour_to_hex(colour: int) -> str:
    # Convert UNTIS number to HEX
    hex_bgr = str(hex(colour)).replace("0x", "")

    # Add beginning zeros if len < 6
    if len(hex_bgr) < 6:
        hex_bgr = "0" * (6 - len(hex_bgr)) + hex_bgr

    # Change BGR to RGB
    hex_rgb = hex_bgr[4:6] + hex_bgr[2:4] + hex_bgr[0:2]

    # Add html #
    return "#" + hex_rgb
