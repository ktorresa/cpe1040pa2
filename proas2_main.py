if __name__ == '__main__':
   def cap_join():
       string_list = []
       string_list.append("calvin")
       string_list.append("and")
       string_list.append("hobbes")
       string_list.append("are")
       string_list.append("the")
       string_list.append("first")
       string_list.append("spacemen")
       string_list.append("on")
       string_list.append("earth")

       cap_string = " ".join(string_list)

       s = cap_string
       print(s.title())


if __name__ == '__main__':
   cap_join()