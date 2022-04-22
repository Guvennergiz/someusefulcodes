import xml.etree.ElementTree as ET
import xlsxwriter

mytree = ET.parse('File-path-with-name-here')
myroot = mytree.getroot()

print(myroot[0])
print(myroot[0][0])
coord_x=[]
coord_y=[]
coord_z=[]
pressure_val=[]

workbook = xlsxwriter.Workbook('xls-file-path-with-name-here',{'strings_to_numbers': True})
worksheet = workbook.add_worksheet()
worksheet.write('A1',"Position X")
worksheet.write('B1',"Position Y")
worksheet.write('C1',"Position Z")
worksheet.write('D1',"Pressure")

i=0
k=0
for poligon in myroot:
  #print("polygon",i)  
  j=0
  for vertex in myroot[i]:
      #print("vertex ",j)
      #print(i,j)
      pos_x=myroot[i][j][0].attrib.pop("x")
      coord_x.append(pos_x)
      pos_y=myroot[i][j][0].attrib.pop("y")
      coord_y.append(pos_y)
      pos_z=myroot[i][j][0].attrib.pop("z")
      coord_z.append(pos_z)
      pres_map=myroot[i][j][1].attrib.pop("PRES")
      pressure_val.append(pres_map)

      worksheet.write('A'+str(k+2),pos_x)
      worksheet.write('B'+str(k+2),pos_y)
      worksheet.write('C'+str(k+2),pos_z)
      worksheet.write('D'+str(k+2),pres_map)
      
      j+=1
      k+=1

  #print("----------------")
  i+=1
  
workbook.close()