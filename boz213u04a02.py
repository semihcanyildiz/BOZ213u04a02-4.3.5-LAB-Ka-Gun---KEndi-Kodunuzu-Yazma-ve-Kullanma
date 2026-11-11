def is_year_leap(year):
    # Artık yıl kontrolü
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # Geçersiz yıl veya ay kontrolü
    if year < 1 or month < 1 or month > 12:
        return None

    # Ayların normal gün sayıları (1. ay -> 31 gün, 2. ay -> 28 gün ...)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    res = days[month - 1]
    
    # Şubat ayı ve artık yıl ise gün sayısını 29 yap
    if month == 2 and is_year_leap(year):
        res = 29
        
    return res

# Test verileri ve kontrol döngüsü
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
