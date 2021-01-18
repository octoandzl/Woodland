from . import Node


class Tree():

	def __init__(self,Node):
		self.root = Node

	@classmethod
	def get_children_Trees(self,cls):
		for c in self.root.children:
			yield cls(c)
