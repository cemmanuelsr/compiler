{
    n1 = 1;
    n2 = 1;
    Print(n1);
    Print(n2);

    i = 0;
    while (i < 100) {
        n3 = n2 + n1;
        Print(n3);
        n1 = n2;
        n2 = n3;
        i = i + 1;
    }
}