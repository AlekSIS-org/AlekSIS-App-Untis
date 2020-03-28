from datetime import date, datetime


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


UNTIS_DATE_FORMAT = "%Y%m%d"


def untis_date_to_date(untis: int) -> date:
    """ Converts a UNTIS date to a python date """
    return datetime.strptime(str(untis), UNTIS_DATE_FORMAT).date()


def date_to_untis_date(date: date) -> int:
    """ Converts a python date to a UNTIS date """
    return int(date.strftime(UNTIS_DATE_FORMAT))


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
