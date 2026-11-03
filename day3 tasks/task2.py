hour = int(input())
minute = int(input())
hour > 23 or minute < 0 or minute > 59:
    print("Invalid time")
else:
if hour < 10:
  print("Late,nopoints")
else:
  print("Training day is over")
  #ليش حسبت 10:00 متأخر؟
  #لان الشرط الاول يغطي الساعات الاقل من 10 واي ساعة تبدا من 10:00 تدخل في شرط elife.
