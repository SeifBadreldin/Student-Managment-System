from utility import *
import json

students={
	"230100575":{
		"name": "seif",
		"code": "230100575",
		"Birthdate": "10/11/2005",
		"age": "18",
		"country": "egypt"
	},
	"230100600":{
		"name": "youssef",
		"code": "230100600",
		"Birthdate": "3/1/2003",
		"age": "21",
		"country": "Usa"
	},
	"230100700":{
		"name": "sama",
		"code": "230100700",
		"Birthdate": "10/6/2009",
		"age": "15",
		"country": "Germany"
	},
	"230100800":{
		"name": "sara",
		"code": "230100800",
		"Birthdate": "10/2/1976",
		"age": "47",
		"country": "Poland"
	},
	"230100900":{
		"name": "mohanad",
		"code": "230100900",
		"Birthdate": "14/4/1975",
		"age": "48",
		"country": "spain"
	}
}
writeJson(students,"students.json")