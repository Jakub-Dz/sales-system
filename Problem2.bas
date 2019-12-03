Attribute VB_Name = "Module1"
' Task objective:
' "The output is expected to be a list of Set1 UID alongside the corresponding UID for the point from Set2."

' Task assumptions:
' 1. Due to the small size of the dataset a simple linear search has been implemented
' 2. X & Y coordinates are numbers and there's no user input, so no checks for variable type have been implemented
' 3. Using variables for input/output cells' address instead of hardcoding


' Declaring global variables for ease of use, as it's a single/short task
Option Explicit
Public shSet1, shSet2, shOutput As Worksheet
Public x_col, y_col, id_col, id1, id2 As String
Public row_start, rows_set1, rows_set2, array_size, i, k, row_min_dist As Integer
Public ix, iy, kx, ky, dist, min_dist As Double
Sub SetGlobalVars()

' Setting tabs/sheets address
Set shSet1 = ThisWorkbook.Sheets("Set1")
Set shSet2 = ThisWorkbook.Sheets("Set2")
Set shOutput = ThisWorkbook.Sheets("Solution")

' Setting rows/columns address
x_col = "A"
y_col = "B"
id_col = "C"
row_start = 2 '<-- First row with data (not headers)

' Checking the number of rows in the dataset
rows_set1 = shSet1.Range(x_col & "1048576").End(xlUp).Row
rows_set2 = shSet2.Range(x_col & "1048576").End(xlUp).Row

End Sub
Sub ClearOutput()

Call SetGlobalVars
shOutput.Range(x_col & row_start & ":" & id_col & "1048576").ClearContents

End Sub
Sub MatchPointAssets()

Application.ScreenUpdating = False ' To speed up the process

Call ClearOutput ' Clear Output sheet & set global variables

' Array/List size calcs - based on Set2 as allocating values from Set1 to Set2 -> Set2 is a 2nd tier loop
array_size = rows_set2 - row_start
ReDim set2_array(array_size)


For i = row_start To rows_set1 ' Take points from Set1, one by one
    
    ix = shSet1.Range(x_col & i).Value2
    iy = shSet1.Range(y_col & i).Value2
    id1 = shSet1.Range(id_col & i).Value2
    
    For k = row_start To rows_set2 ' Calculate distance from Set1 point to each point from Set2
    
        kx = shSet2.Range(x_col & k).Value2
        ky = shSet2.Range(y_col & k).Value2
        dist = Sqr(((ix - kx) ^ 2) + ((iy - ky) ^ 2))
        set2_array(k - row_start) = dist ' Allocating index using the loop's counter
    
    Next k
    
    min_dist = Application.Min(set2_array)
    row_min_dist = (Application.Match(min_dist, set2_array, 0) - 1 + row_start) ' Array index -1 (first index = 0) + starting row
    id2 = shSet2.Range(id_col & row_min_dist).Value2
    
    ' Writing results in the Output tab (! reusing columns address from Input, but can be changed if needed)
    shOutput.Range(x_col & i).Value2 = id1
    shOutput.Range(y_col & i).Value2 = id2
    shOutput.Range(id_col & i).Value2 = Round(min_dist, 2)
    
Next i

Application.ScreenUpdating = True
End Sub


