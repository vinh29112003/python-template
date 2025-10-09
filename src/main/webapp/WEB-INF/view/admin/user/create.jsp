<%@ page contentType = "text/html" pageEncoding="UTF-8" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib uri = "http://java.sun.com/jsp/jstl/core" prefix = "c" %>
<html lang="en">
<head>  
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="/css/LoginAdmin.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Admin</title>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center"> 
            <div class="col-md-6 col-lg-5 form-container">
                <h1 class="text-center">Create a user</h1>
                <form:form method="post" action="/admin/user/create" modelAttribute="newUser">
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email:</label>
                        <form:input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter email" 
                        path="email"/>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password:</label>
                        <form:input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" 
                        path="password"/>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPhoneNumber1" class="form-label">Phone number:</label>
                        <form:input type="text" class="form-control" id="exampleInputPhoneNumber1" placeholder="Phone"
                        path="phone"/>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputFullname1" class="form-label">Full name:</label>
                        <form:input type="text" class="form-control" id="exampleInputFullname1" placeholder="Full name"
                        path="fullName"/>
                    </div>
                    <div class="mb-3">
                        <label for="inputAddress" class="form-label">Address:</label>
                        <form:input type="text" class="form-control" id="inputAddress" placeholder="1234 Main St"
                        path="address"/>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Create</button>
                </form:form>
            </div>
        </div>
    </div>
</body>
</html>
