browsing_session = []

#  Add Items To Stack
browsing_session.append('http://1.com')
browsing_session.append('http://2.com')
browsing_session.append('http://3.com')
print(browsing_session)

# Remove last item in stack
lastItemInStack = browsing_session.pop()
print(browsing_session)
print("redirect", browsing_session[-1])

# Check if stack is empty
if not browsing_session:
    print("Disable Back Button")
