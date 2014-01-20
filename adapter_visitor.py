import os

class Runner(object):
	def __init__(self, name):
		self.name = name
	
	def run(self):
		return "I'm running."

class Swimmer(object):
	def __init__(self, name):
		self.name = name
		
	def swim(self):
		return "I'm swimming."
		
class Thrower(object):
	def __init__(self, name, thing):
		self.name = name
		self.thing = thing
		
	def throw_thing(self):
		return "I'm throwing %s" % self.thing
		
class Adapter(object):
	def __init__(self, obj, adapted_methods):
		self.__dict__.update(adapted_methods)
		self.obj = obj
		
	def __getattr__(self, attr):
		return getattr(self.obj, attr)
		
class Visitor(object):
	def visit(self, node, *args, **kwargs):
		meth = None
		meth_name = 'visit_' +node.obj.__class__.__name__
		meth = getattr(self, meth_name, None)
		if not meth:
			meth = self.generic_visit
		return meth(node, *args, **kwargs)
		
	def generic_visit(self, node, *args, **kwargs):
		print('generic_visit '+ node.__class__.__name__)
		
	def visit_Runner(self, node, *args, **kwargs):
		print('visit_Runner: I am {0} and ' + node.do_sth()).format(node.name) 
	
	def visit_Swimmer(self, node, *args, **kwargs):
		print('visit_Swimmer: I am {0} and ' + node.do_sth()).format(node.name)
	
	def visit_Thrower(self, node, *args, **kwargs):
		print('visit_Thrower: I am {0} and ' + node.do_sth()).format(node.name)

"""
The next block of code is to test Adapter and Visitor classes
"""
def main():
	objects = []
	runner1 = Runner("Usain Bolt")
	swimmer1 = Swimmer("Michael Phelps")
	thrower1 = Thrower("Margus Hunt", "footballs")
	visitor = Visitor()
	objects.append(Adapter(runner1, dict(do_sth=runner1.run)))
	objects.append(Adapter(swimmer1, dict(do_sth=swimmer1.swim)))
	objects.append(Adapter(thrower1, dict(do_sth=thrower1.throw_thing)))
	visitor.visit(Adapter(runner1, dict(do_sth=runner1.run)))
	visitor.visit(Adapter(swimmer1, dict(do_sth=swimmer1.swim)))
	visitor.visit(Adapter(thrower1, dict(do_sth=thrower1.throw_thing)))
	
	for obj in objects:
		print("I am {0} and {1}".format(obj.name, obj.do_sth()))
		
if __name__='__main__':
	main()
