"use client"

import { useEffect, useState } from 'react'

export default function Home() {
  const [users, setUsers] = useState([]);
  useEffect(()=>{
    async function fetchUsers(){
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/`) 
      const json = await res.json()
      // console.log(json[1]);
      setUsers(json[1]);
    }
    fetchUsers()
  },[])
  return (
    users.map((user)=>{
      return(
      <h1 key={user['username']}>{user['username']}</h1>
      )
    })
  )
}
