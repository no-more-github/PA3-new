VTABLE(_Mac) {
    <empty>
    Mac
    _Mac.Crash;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Mac_New) {
memo ''
_Mac_New:
    _T5 = 16
    parm _T5
    _T6 =  call _Alloc
    _T7 = 0
    *(_T6 + 4) = _T7
    *(_T6 + 8) = _T7
    *(_T6 + 12) = _T7
    _T8 = VTBL <_Mac>
    *(_T6 + 0) = _T8
    return _T6
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T9 = 4
    parm _T9
    _T10 =  call _Alloc
    _T11 = VTBL <_Main>
    *(_T10 + 0) = _T11
    return _T10
}

FUNCTION(_Mac.Crash) {
memo '_T0:4 _T1:8 _T2:12 _T2:16 _T4:20'
_Mac.Crash:
    _T12 = *(_T0 + 12)
    *(_T0 + 12) = _T1
    _T13 = *(_T0 + 4)
Exception in thread "main" java.lang.NullPointerException
	at decaf.tac.Tac.toString(Tac.java:287)
	at java.lang.String.valueOf(Unknown Source)
	at java.lang.StringBuilder.append(Unknown Source)
	at decaf.translate.Translater.printTo(Translater.java:70)
	at decaf.Driver.compile(Driver.java:107)
	at decaf.Driver.main(Driver.java:117)
