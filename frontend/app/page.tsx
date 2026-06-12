'use client';
import { useState } from "react"

export default function Home() {

  const [homeform, setHomeForm] = useState("")
  const [homegoals, setHomeGoals] = useState("")
  const [homewinrate, setHomeWinRate] = useState("")
  const [homegoaldiff, setHomeGoalDiff] = useState("")

  const [awayform, setAwayForm] = useState("")
  const [awaygoals, setAwayGoals] = useState("")
  const [awaywinrate, setAwayWinRate] = useState("")
  const [awaygoaldiff, setAwayGoalDiff] = useState("")

  const [prediction, setPrediction] = useState<any>(null)


  const handlePredict = async () => {
    const response = await fetch(
      "https://soccer-score-prediction-xpd7.onrender.com/predict", {
        method: "POST",
        headers: {
          "Content-Type" : "application/json"
        },
        body: JSON.stringify({
          home_form: Number(homeform),
          away_form: Number(awayform),
          home_goal_last5: Number(homegoals),
          away_goal_last5: Number(awaygoals),
          home_win_rate: Number(homewinrate),
          away_win_rate: Number(awaywinrate),
          Home_GD: Number(homegoaldiff),
          Away_GD: Number(awaygoaldiff)          
        })
      }
    )

    const data = await response.json()

    setPrediction(data)

    document.getElementById("target")?.scrollIntoView({ behavior: "smooth" });
  }

  return (
    <div className="min-h-screen text-white flex justify-center items-center flex-col py-12 px-4" style={{background: "linear-gradient(135deg, #0d5c2f 0%, #1a7c3a 50%, #0d5c2f 100%)"}}>
      
      {/* Header */}
      <div className="text-center mb-16">
        <h1 className="text-6xl font-black mb-3" style={{textShadow: "2px 2px 4px rgba(0,0,0,0.5)"}}>⚽ Soccer Match Predictor</h1>
        <div className="h-1 w-32 mx-auto mb-4" style={{background: "linear-gradient(90deg, #fff 0%, #ffd700 50%, #fff 100%)"}}></div>
        <p className="text-xl text-gray-100">Advanced AI-Powered Match Analysis</p>
      </div>

      {/* Match Setup Section */}
      <div className="flex gap-8 mb-12 w-full max-w-5xl justify-center flex-wrap">
        {/* Home Team */}
        <div className="bg-gradient-to-br from-red-700 to-red-900 text-white p-8 rounded-xl shadow-2xl w-80 border-4 border-red-500 transition-all duration-300 hover:scale-105 hover:shadow-red-900/50" style={{boxShadow: "0 10px 30px rgba(139, 0, 0, 0.4)"}}>
          <div className="text-center mb-6">
            <h2 className="text-3xl font-black">🏠 HOME</h2>
            <p className="text-sm text-red-200 mt-1">Enter Team Details</p>
          </div>
          <ul className="space-y-4">
            <li className="flex justify-between items-center bg-red-800/50 p-3 rounded-lg">
              <span className="font-semibold">Form Rating</span>
              <input type="number" value={homeform} onChange={(e) => setHomeForm(e.target.value)} placeholder="0" className="bg-white text-red-900 border-2 border-red-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-red-900" />
            </li>
            <li className="flex justify-between items-center bg-red-800/50 p-3 rounded-lg">
              <span className="font-semibold">Goals (Last 5)</span>
              <input type="number" value={homegoals} onChange={(e) => setHomeGoals(e.target.value)} placeholder="0" className="bg-white text-red-900 border-2 border-red-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-red-900" />
            </li>
            <li className="flex justify-between items-center bg-red-800/50 p-3 rounded-lg">
              <span className="font-semibold">Win Rate (%)</span>
              <input type="number" value={homewinrate} onChange={(e) => setHomeWinRate(e.target.value)} placeholder="0" className="bg-white text-red-900 border-2 border-red-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-red-900" />
            </li>
            <li className="flex justify-between items-center bg-red-800/50 p-3 rounded-lg">
              <span className="font-semibold">Goal Diff</span>
              <input type="number" value={homegoaldiff} onChange={(e) => setHomeGoalDiff(e.target.value)} placeholder="0" className="bg-white text-red-900 border-2 border-red-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-red-900" />
            </li>
          </ul>
        </div>

        {/* VS Divider */}
        <div className="flex flex-col justify-center items-center w-20">
          <div className="text-5xl font-black text-yellow-300" style={{textShadow: "2px 2px 4px rgba(0,0,0,0.7)"}}>VS</div>
          <div className="h-12 w-1 bg-white/30 my-4"></div>
        </div>

        {/* Away Team */}
        <div className="bg-gradient-to-br from-blue-700 to-blue-900 text-white p-8 rounded-xl shadow-2xl w-80 border-4 border-blue-400 transition-all duration-300 hover:scale-105" style={{boxShadow: "0 10px 30px rgba(25, 55, 130, 0.4)"}}>
          <div className="text-center mb-6">
            <h2 className="text-3xl font-black">✈️ AWAY</h2>
            <p className="text-sm text-blue-200 mt-1">Enter Team Statistics</p>
          </div>
          <ul className="space-y-4">
            <li className="flex justify-between items-center bg-blue-800/50 p-3 rounded-lg">
              <span className="font-semibold">Form Rating</span>
              <input type="number" value={awayform} onChange={(e) => setAwayForm(e.target.value)} placeholder="0" className="bg-white text-blue-900 border-2 border-blue-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-blue-900" />
            </li>
            <li className="flex justify-between items-center bg-blue-800/50 p-3 rounded-lg">
              <span className="font-semibold">Goals (Last 5)</span>
              <input type="number" value={awaygoals} onChange={(e) => setAwayGoals(e.target.value)} placeholder="0" className="bg-white text-blue-900 border-2 border-blue-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-blue-900" />
            </li>
            <li className="flex justify-between items-center bg-blue-800/50 p-3 rounded-lg">
              <span className="font-semibold">Win Rate (%)</span>
              <input type="number" value={awaywinrate} onChange={(e) => setAwayWinRate(e.target.value)} placeholder="0" className="bg-white text-blue-900 border-2 border-blue-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-blue-900" />
            </li>
            <li className="flex justify-between items-center bg-blue-800/50 p-3 rounded-lg">
              <span className="font-semibold">Goal Diff</span>
              <input type="number" value={awaygoaldiff} onChange={(e) => setAwayGoalDiff(e.target.value)} placeholder="0" className="bg-white text-blue-900 border-2 border-blue-400 rounded px-3 py-1 w-20 text-right font-bold placeholder-blue-900" />
            </li>
          </ul>
        </div>
      </div>

      {/* Predict Button */}
      <button onClick={handlePredict} className="cursor-pointer bg-gradient-to-r from-yellow-400 via-yellow-300 to-yellow-400 hover:from-yellow-300 hover:via-yellow-200 hover:to-yellow-300 text-gray-900 font-black px-16 py-5 rounded-full shadow-2xl text-2xl transition-all duration-200 transform hover:scale-110 mb-8 border-4 border-yellow-500" style={{boxShadow: "0 8px 20px rgba(255, 215, 0, 0.4)"}}>
        🎯 PREDICT MATCH
      </button>

      {/* Prediction Results */}
      {prediction && (
        <div className="bg-gradient-to-br from-gray-900 to-gray-800 text-white p-10 rounded-xl shadow-2xl w-full max-w-2xl border-4 border-yellow-400">
          <h2 className="text-4xl font-black text-center mb-6 text-yellow-300">🏆 PREDICTION RESULTS</h2>
          <div className="space-y-4">
            <div className="bg-gray-700/80 p-4 rounded-lg border-2 border-yellow-400">
              <p className="text-lg"><span className="font-bold text-yellow-300">🤖 Logistic Regression:</span> <span className="text-2xl font-black ml-2">{prediction["Logistic Regression prediction"]}</span></p>
            </div>
            <div className="bg-gray-700/80 p-4 rounded-lg border-2 border-yellow-400">
              <p className="text-lg"><span className="font-bold text-yellow-300">🌲 Random Forest:</span> <span className="text-2xl font-black ml-2">{prediction["Random Forest prediction"]}</span></p>
            </div>
            <div className="bg-gray-700/80 p-4 rounded-lg border-2 border-yellow-400">
              <p className="text-lg"><span className="font-bold text-yellow-300">⚡ XGBoost:</span> <span className="text-2xl font-black ml-2">{prediction["XGBoost prediction"]}</span></p>
            </div>
          </div>
        </div>
      )}
      <div id="target"></div>
    </div>  
  )
}
