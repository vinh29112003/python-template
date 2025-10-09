package com.java_spring_mvc.laptopshop.repository;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.java_spring_mvc.laptopshop.domain.User;

@Repository
public interface UserRepository extends CrudRepository<User, Long> {
    User save(User hoidanit);
}
