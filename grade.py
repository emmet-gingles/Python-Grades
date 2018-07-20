input = raw_input("Enter score between 0 and 1: ");
try:
    score = float(input);
    if score >= 0 and score <= 1:
        if score >= 0.9:
            print "A";
        elif score >= 0.7:
            print "B";
        elif score >= 0.5:
            print "C";
        elif score >= 0.4:
            print "D";
        elif score < 0.4:
            print "F";
except:
    print "Invalid input";
