#include <stdio.h>


struct Time {
    int days;
    int hours;
    int minutes;
    int seconds;
};


void Convert(struct Time* time, int secs) {
    time->days = secs / (24*60*60);
    secs -= time->days * 24*60*60;

    time->hours = secs / (60*60);
    secs -= time->hours * 60*60;

    time->minutes = secs / 60;
    secs -= time->minutes * 60;
    
    time->seconds = secs;
}


int main() 
{
    struct Time time;
    int seconds;
    scanf("%d", &seconds);
    Convert(&time,seconds);
    printf("%d\n", time.days);
    printf("%d\n", time.hours);
    printf("%d\n", time.minutes);
    printf("%d\n", time.seconds);
    return 0;
}