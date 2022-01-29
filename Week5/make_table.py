def make_table(row, col):
  col_count = 0
  row_count = 0
  
  print("<table>")
  
  while row_count < row:
     print("<tr>")
     while col_count < col:
        print("<td>test</td>")
        col_count += 1
     print("</tr>")
     row_count += 1
     col_count = 0
     
  print("</table>")

make_table(2, 3)
