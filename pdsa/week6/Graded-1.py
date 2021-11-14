
class Min_heap:

	def __init__(self):
		self.size = 0
		self.arr = []

	def isempty(self):
		return not self.arr

	def heapify_up(self):
		"""
		Places the last element in the heap in the right position.
		"""
		v_ind = self.size - 1
		while v_ind > 0:
			v_parent = (v_ind-1)//2
			if self.arr[v_ind][0] < self.arr[v_parent][0]:
				# swap parent and child
				self.arr[v_ind], self.arr[v_parent] = self.arr[v_parent], self.arr[v_ind]
				v_ind = v_parent
			else:
				break

	def heapify_down(self, v_ind):
		"""
		Places the element at a particular index in the right position.
		"""

		while v_ind < self.size:
			left_child_ind = 2 * v_ind + 1
			right_child_ind = 2 * v_ind + 2

			# leaf node
			if left_child_ind > self.size:
				break
			# only has left child
			elif right_child_ind > self.size:
				smaller_child_ind = right_child_ind
			# has both children
			elif self.arr[left_child_ind][0] < self.arr[right_child_ind][0]:
				smaller_child_ind = left_child_ind
			else:
				smaller_child_ind = right_child_ind

			if self.arr[smaller_child_ind][0] < self.arr[v_ind][0]:
				# swap parent and child
				self.arr[smaller_child_ind], self.arr[v_ind] = self.arr[v_ind], self.arr[smaller_child_ind]
			else:
				break

	def insert(self, v):
		self.size += 1
		self.arr.append[v]
		self.heapify_up()

	def delete_min(self):
		min_ = self.arr[0]
		last = self.arr.pop()
		self.size -= 1

		if self.size > 0:
			self.arr[0] = last
			self.heapify_down(0)

		return min_


def mergeKLists(L):
	heap = Min_heap()
	out = []

	# Insert first elements of all lists (the smallest elements)
	for i in range(len(L)):
		heap.insert(
			(L[i][0], i)
			)
	# Number of elements of each list inserted in the heap
	kPointers = [1 for _ in range(len(L))]


	while not heap.isempty():
		tup = heap.delete_min()
		out.append(tup[0])
		list_number = tup[1]

		if kPointers[list_number] < len(L[list_number]):
			tup = (L[list_number][kPointers[list_number]], list_number)
			heap.insert(tup)
			kPointers[list_number] += 1

	return out





