from mind.mind.cluster import *
import inspect
import re

#write mapper train function to pickle mapper model
#load pickle model in mapper map function, then process

class Mapper:
    def mapRE(self,action,data_source,command):
    	#eval(class_name) returns class
    	classes = [cls for cls in eval(action).__subclasses__()]
    	print(classes)

    	for cls in classes:
	    	# get all parameters
	    	my_params = [item[0] for item in cls.__dict__.items() if isinstance(item[1], Param)]# and type(item[1]) != Alias]
	    	my_keywords = [item.keywords for item in cls.__dict__.values() if isinstance(item, Param)]# and type(item) != Alias]
	    	# print(my_keywords)
	    	count = len(my_keywords)
	    	indexes = []
	    	for idx, kw in enumerate(my_keywords):
	    		# print(kw)
	    		for regex in kw:
	    			if regex.search(command):
	    				match = regex.search(command)
	    				count = count - 1
	    				indexes.append(match.groupdict().get("value"))

	    	if(count == 0):
	    		exe = cls()
	    		for i in range(len(indexes)):
	    			x = getattr(exe, my_params[i])
	    			x.value = indexes[i]
	    			# print(my_params[indexes[i]])
	    			# print(params[i][1])
	    			# print(x)
	    		exe.execute(data_source)
	    		break