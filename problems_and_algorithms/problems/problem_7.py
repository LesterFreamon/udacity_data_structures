from typing import Iterator, List, Optional


class RouteTrieNode:
    def __init__(self) -> 'RouteTrieNode':
        """
        # Initialize the node with children as before, plus a handler

        Attributes:
            self.children: the children of the node
            self.handler: the handler of this node
        """

        self.children = {}
        self.handler = None

    def insert(self, path_part: str) -> None:
        """
        # Insert the node as before

        Args:
            path_part: the block of the path
        """

        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler: str) -> 'RouteTrie':
        """
        # Initialize the trie with an root node and a handler,
        this is the root path or home page node

        Attributes:
            self.root:  the root of the paths
            self.handler:  the handler of the path

        Args:
            root_handler: the root handler
        """
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: Iterator[str], handler: str) -> None:
        """
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        Args:
            path_parts: the path blocks
            handler: the handler to be put at the end of the path blocks
        """

        run_node = self.root
        for path_part in path_parts:
            run_node.insert(path_part)
            run_node = run_node.children[path_part]

        run_node.handler = handler

    def find(self, path_parts: Iterator[str]) -> Optional[str]:
        """
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        Args:
            path_parts: Iterator of the path parts

        Returns:
            the handler. None if no handler was found
        """

        run_node = self.root
        for path_part in path_parts:
            if path_part not in run_node.children:
                return None
            else:
                run_node = run_node.children[path_part]

        return run_node.handler


class Router:
    def __init__(self, root_handler: str, no_handler: str) -> 'Router':
        """Create a new RouteTrie for holding our routes
            You could also add a handler for 404 page not found responses as well!

        Attributes:
            self.router:  The router in a trie form
            self.no_handler:  Case of not handler string

        Args:
            root_handler: the root handler
            no_handler: case that there is no handler to be found
        """
        self.router: RouteTrie = RouteTrie(root_handler)
        self.no_handler: str = no_handler

    def add_handler(self, raw_path: str, new_handler: str) -> None:
        """Add a handler for a path
        You will need to split the path and pass the pass parts
        as a list to the RouteTrie

        Args:
            raw_path: the raw path, at the end of which the handler should be set
            new_handler: the new handler to be placed at the end of the path
        """
        path_parts = self.split_path(raw_path)
        self.router.insert(path_parts, new_handler)

    def lookup(self, raw_path: str) -> str:
        """
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        Args:
            raw_path: The path to look in for the handler

        Returns:
            handler
        """

        run_node = self.router.root

        path_parts = self.split_path(raw_path)

        for path_part in path_parts:
            if path_part not in run_node.children:
                return self.no_handler
            run_node = run_node.children[path_part]

        if run_node.handler is None:
            return self.no_handler
        else:
            return run_node.handler

    @staticmethod
    def split_path(raw_path: str) -> Iterator[str]:
        """
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        Args:
            raw_path: a string that should be split by '/'

        Returns:
            parts of the path as iterator
        """

        path_parts = raw_path.split('/')
        return filter(lambda x: len(x) > 0, path_parts)  # no need to keep empty parts