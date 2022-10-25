{
    var n1, n2 : i32;
    n1 = 1;
    n2 = 1;
    Print(n1);
    Print(n2);

    var i : i32;
    i = 0;

    var n3 : i32;
    while (i < 100) {
        n3 = n2 + n1;
        Print(n3);
        n1 = n2;
        n2 = n3;
        i = i + 1;
    }
}