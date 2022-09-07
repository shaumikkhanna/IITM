console.log("Hello world!");

// q4
const obj = {
	name: "Rohit",
	changeName: function(name) {
		this.name = name;
	},
}

obj.changeName("Mohit");
console.log(obj.name);

// q5
const x = {name: "rohit"}
x.name = "Mohit";
console.log(x.name);

// q6
const obj2 = {
	name: "Rohit",
	changeName: (name) => {
		this.name = name;
	},
}

obj2.changeName("Mohit");
console.log(obj2.name);

// q7
const obj3 = {
	name: "Rohit",
	arrowFunction: null,
	normalfunction: function() {
		this.arrowFunction = () => {
			console.log(this.name);
		}
	},
}

obj3.normalfunction();
obj3.arrowFunction();


// q08
setTimeout(() => console.log('hello from st1'), 0);
console.log('main1');
setTimeout(() => console.log('hello from st2'), 0);
console.log('main2');

// q10
let startNamePrinter = (name) => {
	let x = name.split('').reverse();
	console.log('start');
	let handler = setInterval(() => {
		let y = x.pop();
		console.log(y);
	}, 1000)

	setTimeout(() => {
		clearInterval(handler);
	}, (name.length + 1) * 1000)
}

startNamePrinter('Orange');
