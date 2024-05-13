class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    def dfs_search(node,id):
      if node['id'] == id:
        return node
      for child in node['children']:
        result = dfs_search(child, id)
        if result:
          return result
      return None
    return dfs_search(self.root, id)