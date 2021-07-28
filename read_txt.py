import os , sys 
		
def getInfo(file_path):

	with open(file_path,"r") as file_object:
		content = file_object.read()	
		print(content)

if __name__ == "__main__":

	file_path = sys.argv[-1]
	getInfo(file_path)	