


class Node(object):

	def __init__(self, parent = None, children = None, value = None, isRoot = None, isLeaf = False):
		self.parent = parent 
		self.value = value 
		self.children = children 
		self.isLeaf = isLeaf
		self.isRoot = isRoot
		
	@property
	def get_value(self):
		return self.value

	@property
	def get_parent(self):
		return self.parent
	
	@property
	def get_children(self):
		return self.children
	
	@property
	def is_root(self):
		return self.is_root
	
	@property
	def isLeaf(self):
		return self.isLeaf

	@property
	def set_value(self,value):
		self._value = value

	@property
	def set_parent(self,node):
		self._parent = node

	@property
	def set_children(self,children):
		self._children = children

	@property
	def set_root(self):
		self.set_parent(None) 
		self._isRoot = True

	@property
	def set_leaf(self):
		self.set_children(None) 
		self._isLeaf = True
