package com.java_spring_mvc.laptopshop.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.java_spring_mvc.laptopshop.domain.User;
import com.java_spring_mvc.laptopshop.services.UserService;




@Controller
public class UserController {

    @Autowired
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
 
    }
    
    @RequestMapping(value="/admin/user/", method=RequestMethod.GET)
    public String getUserPage(Model model) {
        List<User> users = this.userService.getAllUsers();
        System.out.println("check user: "+users);
        model.addAttribute("users1",users);
        return "/admin/user/table-user";
    }
    
    
    @RequestMapping("/admin/user/create")//get
    public String getCreateUserPage(Model model){
        // model.addAttribute("vinh", "abc");
        model.addAttribute("newUser",new User());
        return "admin/user/create";
    }

    @RequestMapping(value = "/admin/user/create", method=RequestMethod.POST)
    public String createUserPage(Model model,@ModelAttribute("newUser") User hoidanit){
        this.userService.handleSaveUser(hoidanit);
        return "redirect:/admin/user/";
    }

}
