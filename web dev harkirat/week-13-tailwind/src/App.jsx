import './App.css';
import Button from './components/button';
import InputBtn from './components/inputBtn';

function App() {

	return (
		<div className='bg-blue-950 h-screen'>
			<br />
			<br />
			<br />
			<br />
			<div className='flex flex-col gap-8'>
				<InputBtn type={"text"} placeholder={"Enter your email"} />
				<Button disabled={false}>Continue</Button>
			</div>
		</div>
	);
}

export default App;
