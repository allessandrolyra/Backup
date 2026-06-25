import { Link } from 'react-router-dom'

export default function Dashboard() {
  return (
    <div>
      <h1 className="text-xl sm:text-2xl font-bold mb-6">Painel do Paciente</h1>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <Link
          to="/agendar"
          className="block p-6 min-h-[100px] rounded-xl bg-white border border-slate-200 shadow-sm hover:shadow-md hover:border-emerald-200 transition"
        >
          <h3 className="font-semibold text-emerald-700 mb-2">Agendar consulta</h3>
          <p className="text-sm text-slate-600">Escolha o médico e horário disponível.</p>
        </Link>
        <Link
          to="/minhas-consultas"
          className="block p-6 min-h-[100px] rounded-xl bg-white border border-slate-200 shadow-sm hover:shadow-md hover:border-emerald-200 transition"
        >
          <h3 className="font-semibold text-emerald-700 mb-2">Minhas consultas</h3>
          <p className="text-sm text-slate-600">Visualize, confirme ou cancele.</p>
        </Link>
      </div>
    </div>
  )
}
