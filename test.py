from utility import *
import json

courses={"CET111": {"code": "CET111", "name": "computer programming", "maxdegree": "100"}, "EPT111": {"code": "EPT111", "name": "CAD", "maxdegree": "100"}, "GEN11": {"code": "GEN11", "name": "Apllied Maths", "maxdegree": "100"}, "Hum121": {"code": "Hum121", "name": "Law", "maxdegree": "100"}}
writeJson(courses,"courses.json")