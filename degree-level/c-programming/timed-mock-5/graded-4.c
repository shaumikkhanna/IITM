#include <stdio.h>


enum Month {
	January = 1,
	February,
	March,
	April,
	May,
	June,
	July,
	August,
	September,
	October,
	November,
	December
};


int daysInMonth(int year, int month) {
	switch (month) {
		case January:
			return 31;
		case February:
			if (year % 4 == 0) {
				if (year % 100 == 0) {
					if (year % 400 == 0) {
						return 29;
					} else {
						return 28;
					}
				} else {
					return 29;
				}
			} else {
				return 28;
			}
		case March:
			return 31;
		case April:
			return 30;
		case May:
			return 31;
		case June:
			return 30;
		case July:
			return 31;
		case August:
			return 31;
		case September:
			return 30;
		case October:
			return 31;
		case November:
			return 30;
		case December:
			return 31;
	}
}


int main()
{
	int year;
	enum Month month;
	scanf("%d %u", &year,&month);
	printf("%d\n", daysInMonth(year,month));
	return 0;
}