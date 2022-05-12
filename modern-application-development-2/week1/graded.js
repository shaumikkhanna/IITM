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
	name: 'Rohit',
	changeName: (name) => {
		this.name = name;
	},
}

obj2.changeName('Mohit');
console.log(obj2.name);

// q7
const obj3 = {
	name: 'Rohit',
	arrowFunction: null,
	normalfunction: function() {
		this.arrowFunction = () => {
			console.log(this.name);
		}
	},
}

obj3.normalfunction()
obj3.arrowFunction()
