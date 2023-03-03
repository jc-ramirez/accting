from resources import *

min_headers = ["cta or apt", "", "salida", "entrada"]
  
if __name__ == "__main__":
  opts = find_sheet()
  
  if len(opts) > 1:
    path = input(f"Con que cuenta te gustaria trabajar {*opts,}?\n")
    path = path + ".xlsx"

  elif len(opts) == 1:
    opciones =input(f"Si te gustaria habrir {opts[0]}, escribi, '{opts[0]}'' o si te gustraria comencar otra cuenta, escribi 'otra'.\n")
    if opciones == opts[0]:
      path = opts[0] + ".xlsx"
    else:
      path = input("Por favor entra el nombre para iniciar (ejemplo '9027'.)") + ".xlsx"

  else:
    path = input("No existen cuentas, vamos iniciar una. Por favor entra un nombre para iniciar (ejemplo '9027'.\n") + ".xlsx"
    wb = openpyxl.Workbook()
    wb.save(path)
    hdrs = init_headers()
    print(hdrs)

    
 
  wb = load_workbook(path)
  if firstmonth(wb, mth):
    st_month = input("Esta es la primera vez que inicias sesión con esta cuenta este mes. Te gustaria empezar la cuenta mensual?\nEscribi 'si' o 'no'\n")

    if st_month.lower() == 'si':
      ws = wb.create_sheet(f"{mth}")
      wb.active = ws
      for i in range(len(min_headers)):
        create_col(ws, i + 1, min_headers[i])
      #sheet = wb.active
      wb.save(path)

      print(f"Worksheet names: {wb.sheetnames}")
      #wr_values(d, f"{mth}", "A2:B5")

  else:
    st_month = input("Con que te puedeo ayudar?\n")







