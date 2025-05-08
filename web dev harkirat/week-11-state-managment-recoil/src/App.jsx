import './App.css';
import { RecoilRoot, useSetRecoilState, useRecoilValue } from 'recoil';
import { counterAtom } from './store/atoms/counter';

function App() {

	return (
		<RecoilRoot>
			<Counter />
		</RecoilRoot>
	);

	function Counter() {
		const count = useRecoilValue(counterAtom);

		return <div>
			<Increase />
			<Decrease />
			<CurrentCount />
		</div>;
	}

	function CurrentCount() {
		return <div>{count}</div>;
	}

	function Increase() {
		const setCount = useSetRecoilState(counterAtom);
		function change(add_sub) {
			setCount(c => c + add_sub);
		}
		return <div>
			<button onClick={() => change(1)}>increase</button>
		</div>;
	}

	function Decrease() {
		const setCount = useSetRecoilState(counterAtom);
		function change(add_sub) {
			setCount(c => c + add_sub);
		}
		return <div>
			<button onClick={() => change(-1)}>decrease</button>
		</div>;
	}
}

export default App;
