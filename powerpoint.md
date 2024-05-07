# Powerpoint

## Change the spell check language for all slides

- Press Alt + F11.
- Create a new macro with this code:

```
Option Explicit
Public Sub ChangeSpellCheckingLanguage()
    Dim j As Integer, k As Integer, scount As Integer, fcount As Integer
    scount = ActivePresentation.Slides.Count
    For j = 1 To scount
        fcount = ActivePresentation.Slides(j).Shapes.Count
        For k = 1 To fcount
            If ActivePresentation.Slides(j).Shapes(k).HasTextFrame Then
                ActivePresentation.Slides(j).Shapes(k) _
                .TextFrame.TextRange.LanguageID = msoLanguageIDEnglishUS
            End If
        Next k
    Next j
End Sub
```

- Run it.

See: https://www.youtube.com/watch?v=ME1EPXFe_fc
