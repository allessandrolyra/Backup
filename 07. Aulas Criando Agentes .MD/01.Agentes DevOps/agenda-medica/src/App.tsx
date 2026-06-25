import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { supabase } from './lib/supabase'
import type { User } from '@supabase/supabase-js'
import Layout from './components/Layout'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import BookAppointment from './pages/BookAppointment'
import MyAppointments from './pages/MyAppointments'
import Admin from './pages/Admin'
import Health from './pages/Health'

function App() {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })
    const { data: { subscription } } = supabase.auth.onAuthStateChange((_e, session) => {
      setUser(session?.user ?? null)
    })
    return () => subscription.unsubscribe()
  }, [])

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600" />
      </div>
    )
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout user={user} />}>
          <Route index element={<Home />} />
          <Route path="login" element={user ? <Navigate to="/dashboard" /> : <Login />} />
          <Route path="register" element={user ? <Navigate to="/dashboard" /> : <Register />} />
          <Route
            path="dashboard"
            element={user ? <Dashboard /> : <Navigate to="/login" />}
          />
          <Route
            path="agendar"
            element={user ? <BookAppointment /> : <Navigate to="/login" />}
          />
          <Route
            path="minhas-consultas"
            element={user ? <MyAppointments /> : <Navigate to="/login" />}
          />
          <Route path="admin/*" element={user ? <Admin /> : <Navigate to="/login" />} />
          <Route path="health" element={<Health />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
