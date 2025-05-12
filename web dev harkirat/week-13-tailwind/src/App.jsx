import './App.css';

function App() {

	return (
		<main className='bg-blue-950 h-screen w-screen flex flex-col items-center'>
			<h1 className='mt-28'>webinar.gg</h1>
			<h2>Verify your age</h2>
			<p>pls conferm ur dob this data will not be stored</p>
			<input className='bg-blue-900 outline-2-red' type="date" name="" value='Your Birth Date' id="" />
			<input className='bg-gray-600' type="submit" value="submit" />
			
		</main>
	);
}

export default App;
