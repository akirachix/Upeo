import React from 'react'
import { PrimaryNav, MenuLink, Menu, Hamburger } from './NavElement'
import './navbar.css';
const Navbar = () => {
    return (
    <>
    <PrimaryNav>
    <Hamburger/>
        <Menu>
          <MenuLink to="/+New Answers" activeStyle>
            New Answers
          </MenuLink>
          <MenuLink to="/+Upload file" activeStyle>
            Upload file
          </MenuLink>
          <MenuLink to="/Questions" activeStyle>
            Questions
          </MenuLink>
        </Menu>
      </PrimaryNav>
      </>
  )
}
export default Navbar

     
    






