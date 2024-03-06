import datetime

def days_until(date_str):
    """
    计算距离指定日期还有多少天
    """
    today = datetime.date.today()
    target_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    delta = target_date - today
    return delta.days
