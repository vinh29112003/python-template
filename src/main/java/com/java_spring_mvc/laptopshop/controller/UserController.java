package com.java_spring_mvc.laptopshop.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.java_spring_mvc.laptopshop.services.UserService;


@Controller
public class UserController {

    @Autowired
    private UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @RequestMapping("/")
    public String getHomePage(Model model){
        model.addAttribute("vinh", "abc");
        return "Hello";
    }
}
