package com.java_spring_mvc.laptopshop.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.java_spring_mvc.laptopshop.domain.User;
import com.java_spring_mvc.laptopshop.repository.UserRepository;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository){
        this.userRepository = userRepository;
    }
    public String handleHello() {
        return "Hello";
    }

    public List<User> getAllUsers(){
        return (List<User>) this.userRepository.findAll();
    }

    public List<User> getAllUsersByEmail(String email){
        return (List<User>) this.userRepository.findAll();
    }

    public User handleSaveUser(User user) {
        User eric = this.userRepository.save(user);
        System.out.println(eric);
        return eric;
        
    }
}
