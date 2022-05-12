/*
 * calculateSimpleInterest calculates and returns the simple interest
 * (floor value) for a fixed deposit. Formula used is,

 * calculateSimpleInterest calculates and returns the simple interest
 * for a fixed deposit. Formula used is,
 * Simple Interest: P X R X T / 100
 *   where:
 *   P = Principal
 *   I = Daily interest rate
 *   N = Number of days
 *
 *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
 *
 * @param {number} principal  - Principal amount
 * @param {number} dailyInterest  - daily interest rate
 * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @return {number} interest
*/

/*
 * calculateCompoundInterest calculates and returns the compound interest
 * (floor value) for a fixed deposit. Formula used is,
 *   Compound Interest=P[(1+I/100)^N - 1]
 *   where:
 *   P = Principal
 *   I = Daily interest rate
 *   N = Number of days
 *
 *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
 *
 * @param {number} principal  - Principal amount
 * @param {number} dailyInterest  - daily interest rate
 * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @return {number} interest
*/

/*
 * extraAmountPercentage calculates and returns the extra amount percentage borrower will have to pay in case of
 * compound interest (floor value) in comparison to the simple interest for a fixed deposit.

 *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
 *
 * @param {number} principal  - Principal amount
 * @param {number} dailyInterest  - Daily interest rate.
 * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @return {number} percentage
*/

function numberOfDays(startingDate, endingDate) {
	let s = new Date(startingDate);
	let e = new Date(endingDate);
	let days = (e.getTime() - s.getTime()) / (1000*60*60*24);
    console.log(days);
    return days;
}

function calculateSimpleInterest(
	principal,
	dailyInterest,
	startingDate,
	endingDate
) {
interest = principal * dailyInterest * numberOfDays(startingDate, endingDate) / 100;
if (interest == NaN) {
	return -1;
}
return Math.floor(interest);
}

function calculateCompoundInterest(
	principal,
	dailyInterest,
	startingDate,
	endingDate
) {
try {
	interest = principal * ((1 + dailyInterest/100)**numberOfDays(startingDate, endingDate) - 1);
	return Math.floor(interest);
} catch(err) {
	return -1;
}

}

function extraAmountPercentage(
	principal,
	dailyInterest,
	startingDate,
	endingDate
) {

let compound = calculateCompoundInterest(principal, dailyInterest, startingDate, endingDate);
let simple = calculateSimpleInterest(principal, dailyInterest, startingDate, endingDate);
let percentage = Math.floor((compound/simple - 1)*100);
return Math.floor(percentage);

}

console.log(calculateSimpleInterest(20000, 1, "2020-03-12", "2020-05-11"));
console.log(calculateSimpleInterest(20000, 1, "30", "2020-05-11"));


