export default function SSTTrainingControl() {
  const cards = [
    { title: 'Total Funcionários', value: 6 },
    { title: 'Treinamentos Válidos', value: 5 },
    { title: 'Próximos do Vencimento', value: 3 },
    { title: 'Treinamentos Vencidos', value: 4 },
  ];

  const funcionarios = [
    { nome: 'Carlos Alberto Silva', matricula: 'MAT-001' },
    { nome: 'Fernanda Oliveira', matricula: 'MAT-002' },
    { nome: 'Ricardo Mendes', matricula: 'MAT-003' },
    { nome: 'Ana Paula Santos', matricula: 'MAT-004' },
    { nome: 'Marcos Pereira', matricula: 'MAT-005' },
    { nome: 'Juliana Costa', matricula: 'MAT-006' },
  ];

  return (
    <div className="min-h-screen bg-black text-white p-4 font-sans">
      <div className="max-w-md mx-auto space-y-6">

        {/* LOGIN */}
        <div className="bg-zinc-900 rounded-3xl p-6 shadow-2xl border border-zinc-800">
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-full bg-red-600 flex items-center justify-center text-2xl font-bold">
              S
            </div>
          </div>

          <h1 className="text-2xl font-bold text-center">Welcome to SST Training Control</h1>
          <p className="text-zinc-400 text-center mt-2">Sign in to continue</p>

          <button className="w-full mt-6 bg-white text-black py-3 rounded-xl font-semibold hover:opacity-90 transition">
            Continue with Google
          </button>

          <div className="my-4 text-center text-zinc-500">OR</div>

          <input
            type="email"
            placeholder="Email"
            className="w-full bg-zinc-800 border border-zinc-700 rounded-xl p-3 mb-3"
          />

          <input
            type="password"
            placeholder="Password"
            className="w-full bg-zinc-800 border border-zinc-700 rounded-xl p-3 mb-4"
          />

          <button className="w-full bg-red-600 hover:bg-red-700 transition py-3 rounded-xl font-bold">
            Sign in
          </button>

          <div className="text-center text-sm text-zinc-400 mt-4">
            Forgot password? <span className="text-red-500">Sign up</span>
          </div>
        </div>

        {/* DASHBOARD */}
        <div>
          <h2 className="text-3xl font-bold">Dashboard</h2>
          <p className="text-zinc-400 mb-4">Visão geral do controle de treinamentos SST</p>

          <div className="grid grid-cols-2 gap-4">
            {cards.map((card, index) => (
              <div
                key={index}
                className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-lg"
              >
                <p className="text-zinc-400 text-sm">{card.title}</p>
                <h3 className="text-3xl font-bold mt-2">{card.value}</h3>
              </div>
            ))}
          </div>
        </div>

        {/* FUNCIONÁRIOS */}
        <div>
          <div className="flex items-center justify-between mb-4">
            <div>
              <h2 className="text-3xl font-bold">Funcionários</h2>
              <p className="text-zinc-400">Gerencie os funcionários da empresa</p>
            </div>

            <button className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded-xl font-semibold">
              + Novo Funcionário
            </button>
          </div>

          <input
            placeholder="Buscar por nome, matrícula, cargo..."
            className="w-full bg-zinc-900 border border-zinc-700 rounded-xl p-3 mb-4"
          />

          <div className="space-y-3">
            {funcionarios.map((funcionario, index) => (
              <div
                key={index}
                className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 flex items-center justify-between"
              >
                <div>
                  <h3 className="font-semibold">{funcionario.nome}</h3>
                  <p className="text-zinc-400 text-sm">Desenvolvedor</p>
                </div>

                <div className="text-sm text-zinc-500">
                  {funcionario.matricula}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* RELATÓRIOS */}
        <div>
          <h2 className="text-3xl font-bold">Relatórios</h2>
          <p className="text-zinc-400 mb-4">
            Exporte e analise dados de treinamentos e conformidade
          </p>

          <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 mb-4">
            <h3 className="text-red-500 text-4xl font-bold">42%</h3>
            <p className="text-zinc-400 mt-2">Vencimento Geral</p>
          </div>

          <div className="flex gap-2">
            <button className="bg-red-600 px-4 py-2 rounded-xl">Vencidos</button>
            <button className="bg-zinc-800 px-4 py-2 rounded-xl">Importantes</button>
            <button className="bg-zinc-800 px-4 py-2 rounded-xl">Todos</button>
          </div>
        </div>

        {/* EQUIPE */}
        <div>
          <h2 className="text-3xl font-bold mb-4">Equipe de Desenvolvimento</h2>

          <div className="space-y-4">
            {['Kenny Santos', 'Maria Oliveira', 'Lucas Andrade'].map((nome, index) => (
              <div
                key={index}
                className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5"
              >
                <div className="w-14 h-14 rounded-full bg-red-700 flex items-center justify-center text-xl font-bold mb-3">
                  {nome.charAt(0)}
                </div>

                <h3 className="text-xl font-semibold">{nome}</h3>
                <p className="text-zinc-400">Equipe SST Training Control</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}


