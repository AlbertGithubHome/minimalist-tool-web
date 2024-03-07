from datetime import datetime
from lunarcalendar import Solar, Lunar, Converter

def get_days_until_holidays():
    # 定义节日和日期的字典
    holidays = {
        '元旦': ("solar", 1, 1),
        '春节': ("lunar", 1, 1),
        '清明节': ("lunar", 2, 26),
        '劳动节': ("solar", 5, 1),
        '中秋节': ("lunar", 8, 15),
        '国庆节': ("solar", 1, 1),
    }

    # 获取今天的日期和农历日期
    today = datetime.now()
    today_lunar = Converter.Solar2Lunar(Solar(today.year, today.month, today.day))

    # 计算距离每个节日最近的日期的天数
    days_until = {}
    for holiday, date in holidays.items():
        calender, month, day = date
        if "solar" == calender:
            # 公历日期的节日
            holiday_date = Solar(today.year, month, day).to_date()
            if holiday_date < today.date():
                holiday_date = Solar(today_lunar.year + 1, month, day).to_date()
        else:
            # 农历日期的节日
            holiday_date = Lunar(today_lunar.year, month, day).to_date()
            if holiday_date < today.date():
                holiday_date = Lunar(today_lunar.year + 1, month, day).to_date()
        days_until[holiday] = (holiday_date - today.date()).days

    return days_until