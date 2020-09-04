import copy


class SuffixAutomaton:
    def __init__(self):
        self.edges = []  # edges[i]  : the labeled edges from node i
        self.link = []  # link[i]   : the parent of i
        self.length = (
            []
        )  # length[i] : the length of the longest string in the ith class
        self.last = 0  # the index of the equivalence class of the whole string

    def build(self, string):
        # add the initial node
        self.edges.append({})
        self.link.append(-1)
        self.length.append(0)

        for i in range(len(string)):
            # construct r
            self.edges.append({})
            self.length.append(i + 1)
            self.link.append(0)
            r = len(self.edges) - 1

            # add edges to r and find p with link to q
            p = self.last
            while p >= 0 and string[i] not in self.edges[p]:
                self.edges[p][string[i]] = r
                p = self.link[p]

            if p != -1:
                q = self.edges[p][string[i]]

                if self.length[p] + 1 == self.length[q]:
                    # we do not have to split q, just set the correct suffix link
                    self.link[r] = q
                else:
                    # we have to split, add q
                    self.edges.append(copy.deepcopy(self.edges[q]))  # copy edges of q
                    self.length.append(self.length[p] + 1)
                    self.link.append(self.link[q])
                    qq = len(self.edges) - 1
                    self.link[q] = qq
                    self.link[r] = qq

                    while p >= 0 and self.edges[p][string[i]] == q:
                        self.edges[p][string[i]] = qq
                        p = self.link[p]
            self.last = r
        print(self.edges)


a = SuffixAutomaton()
a.build("doggo")
