<%@ page contentType="text/html" pageEncoding="UTF-8" %>
  <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
      <html lang="en">

      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <link rel="stylesheet" href="/css/LoginAdmin.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title>Table Users</title>
      </head>

      <body>
        <div class="container mt-5">
          <div class="row">
            <div class="col-12 mx-auto">
              <div class="d-flex justify-content-between">
                <h3>Table Users</h3>
                <a href="/admin/user/create" class="btn btn-primary">Create a user</a>
              </div>
              <hr />
              <table class="table table-hover table-bordered">
                <thead>
                  <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Email</th>
                    <th scope="col">fullName</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody>

                  <c:forEach items="${users1}" var="user">
      
                    <tr>
                      <td>${user.id}</td>
                      <td>${user.email}</td>
                      <td>${user.fullName}</td>
                      <td>
                        <button class="btn btn-success">View</button>
                        <button class="btn btn-warning">Update</button>
                        <button class="btn btn-danger">Delete</button>
                      </td>
                    </tr> 
                  </c:forEach>
                 

                </tbody>
              </table>
            </div>
          </div>
        </div>
      </body>

      </html>