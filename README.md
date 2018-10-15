#version-1.0.1
# Python(Version 3.7.0)+Django(Version 2.0.4)+Sqlite 
# demo project on python django 
# Funtionality added in this project

# Default Admin Panel http://127.0.0.1:8000/admin/

# User Login http://127.0.0.1:8000/accounts/login/
# User Registration http://127.0.0.1:8000/accounts/registration/
# User Profile http://127.0.0.1:8000/accounts/profile/

# Dynamic Menu (Category Names in Menu)

# Add Blog(Title, Text) http://127.0.0.1:8000/blog/add
# Blog Listing with pagination http://127.0.0.1:8000/blog/
# Catgory wise Blog Listing with pagination http://127.0.0.1:8000/blog/category/category-1
# Blog Detail Page http://127.0.0.1:8000/blog/2/
# Blog Detail Page http://127.0.0.1:8000/blog/slug/
# Update Blog http://127.0.0.1:8000/blog/2/edit/
# Update Blog http://127.0.0.1:8000/blog/slug/edit/
# URL id wise and slug wise

# REST API- Blog listing with pagination(GET Method http://127.0.0.1:8000/api/v1/blog?limit=10)
# REST API- ADD Blog(POST Method,  BODY:  title(string), text(string), author(int), http://127.0.0.1:8000/api/v1/blog/add)
# REST API- Single Blog Details(POST Method,  BODY:  pk(int), http://127.0.0.1:8000/api/v1/blog/single)
# REST API- UPDATE Blog(POST Method,  BODY:  pk(int), title(string), text(string), author(int), http://127.0.0.1:8000/api/v1/blog/single/update)
# REST API - DELETE Blog(POST Method, BODY: pk(int), author(int), http://127.0.0.1:8000/api/v1/blog/single/delete)
# REST API - Catgory Wise Blogs (POST METHOD, BODY: pk(int)) http://127.0.0.1:8000/api/v1/blog/category/posts
# REST API - ALL Category Listing (GET METHOD) http://127.0.0.1:8000/api/v1/blog/category


# Facing Issue
# REST API->Post Method ->PostSerializer ->Pagination Not Working(When using GET Method without function pagination working)
# In case of update blog->image path "blog/06/abc.jpg"(Working Properly)
  In case of add blog-> image path "blog/None/abc.jpg"(Primary Key is None in this case)
  
# Editor (WYSIWYG)->Not Working
# Django with MYSQL Database
# Send Email Not Working