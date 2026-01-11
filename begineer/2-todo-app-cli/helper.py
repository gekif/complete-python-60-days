import time

def get_timestamp():
    months = {
        "01": "Januari", "02": "Februari", "03": "Maret",
        "04": "April", "05": "Mei", "06": "Juni",
        "07": "Juli", "08": "Agustus", "09": "September",
        "10": "Oktober", "11": "November", "12": "Desember"
    }

    day = time.strftime("%d")
    month_num = time.strftime("%m")
    year = time.strftime("%Y")
    clock = time.strftime("%H:%M:%S")

    month_name = months[month_num]
    return f"{day} {month_name} {year}, {clock}"
