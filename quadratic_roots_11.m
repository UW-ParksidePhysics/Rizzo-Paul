% Author: Paul Rizzo & Nora Nichols
a = input("What is a? ");
b = input("What is b? ");
c = input("What is c? ");


D2 = b ^ 2 - 4 * a * c;
if a == 0
    disp('a Cannot Equal Zero')
end

if D2 >= 0
    D = sqrt(D2);
    x1 = (-b - D) / (2 * a);
    x2 = (2 * c) / (-b - D);
    R = [x1, x2];
    disp("test_roots_float")
    disp(R)

elseif D2 < 0
    D2 = -D2;
    D = (sqrt(D2) / (2 * a));
    b2 = -b / (2 * a);
    disp("test_roots_complex")
    fprintf('%g %s %g %s',b2, '+', D, 'i ');fprintf('%g %s %g %s', b2, '-', D, 'i');
    fprintf('\n');
end
