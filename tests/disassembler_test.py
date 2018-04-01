from unittest import TestCase

from mythril.disassembler.disassembly import Disassembly
from mythril.ether import util
from tests import *

def _compile_to_code(input_file):
    compiled = util.get_solc_json(str(input_file))
    code = list(compiled['contracts'].values())[0]['bin-runtime']
    return code

class DisassemblerTestCase(TestCase):

    def test_instruction_list(self):
        code = "0x606060405236156100ca5763ffffffff60e060020a600035041663054f7d9c81146100d3578063095c21e3146100f45780630ba50baa146101165780631a3719321461012857806366529e3f14610153578063682789a81461017257806389f21efc146101915780638da5cb5b146101ac5780638f4ffcb1146101d55780639a1f2a5714610240578063b5f522f71461025b578063bd94b005146102b6578063c5ab5a13146102c8578063cc424839146102f1578063deb077b914610303578063f3fef3a314610322575b6100d15b5b565b005b34610000576100e0610340565b604080519115158252519081900360200190f35b3461000057610104600435610361565b60408051918252519081900360200190f35b34610000576100d1600435610382565b005b3461000057610104600160a060020a03600435166103b0565b60408051918252519081900360200190f35b346100005761010461041e565b60408051918252519081900360200190f35b3461000057610104610424565b60408051918252519081900360200190f35b34610000576100d1600160a060020a036004351661042b565b005b34610000576101b961046f565b60408051600160a060020a039092168252519081900360200190f35b3461000057604080516020600460643581810135601f81018490048402850184019095528484526100d1948235600160a060020a039081169560248035966044359093169594608494929391019190819084018382808284375094965061048595505050505050565b005b34610000576100d1600160a060020a03600435166106e7565b005b346100005761026b60043561072b565b60408051600160a060020a0390991689526020890197909752878701959095526060870193909352608086019190915260a085015260c084015260e083015251908190036101000190f35b34610000576100d160043561077a565b005b34610000576101b9610830565b60408051600160a060020a039092168252519081900360200190f35b34610000576100d160043561083f565b005b34610000576101046108a1565b60408051918252519081900360200190f35b34610000576100d1600160a060020a03600435166024356108a7565b005b60015474010000000000000000000000000000000000000000900460ff1681565b600681815481101561000057906000526020600020900160005b5054905081565b600054600160a060020a036301000000909104811690331681146103a557610000565b60038290555b5b5050565b6005546040805160006020918201819052825160e260020a631d010437028152600160a060020a03868116600483015293519194939093169263740410dc92602480830193919282900301818787803b156100005760325a03f115610000575050604051519150505b919050565b60035481565b6006545b90565b600054600160a060020a0363010000009091048116903316811461044e57610000565b60018054600160a060020a031916600160a060020a0384161790555b5b5050565b60005463010000009004600160a060020a031681565b6000600060006000600060006000600160149054906101000a900460ff16156104ad57610000565b87600081518110156100005760209101015160005460f860020a918290048202975002600160f860020a031990811690871614156105405760009450600196505b600587101561053057878781518110156100005790602001015160f860020a900460f860020a0260f860020a900485610100020194505b6001909601956104ee565b61053b8b868c610955565b6106d6565b600054610100900460f860020a02600160f860020a0319908116908716141561069e57506001955060009250829150819050805b60058710156105b657878781518110156100005790602001015160f860020a900460f860020a0260f860020a900481610100020190505b600190960195610574565b600596505b60098710156105fd57878781518110156100005790602001015160f860020a900460f860020a0260f860020a900484610100020193505b6001909601956105bb565b600996505b600d87101561064457878781518110156100005790602001015160f860020a900460f860020a0260f860020a900483610100020192505b600190960195610602565b600d96505b601187101561068b57878781518110156100005790602001015160f860020a900460f860020a0260f860020a900482610100020191505b600190960195610649565b61053b8b828c878787610bc4565b6106d6565b60005462010000900460f860020a02600160f860020a031990811690871614156106d15761053b8b8b610e8e565b6106d6565b610000565b5b5b5b5b5050505050505050505050565b600054600160a060020a0363010000009091048116903316811461070a57610000565b60058054600160a060020a031916600160a060020a0384161790555b5b5050565b600760208190526000918252604090912080546001820154600283015460038401546004850154600586015460068701549690970154600160a060020a03909516969395929491939092909188565b600081815260076020526040812054600160a060020a0390811690331681146107a257610000565b600083815260076020526040902080546004820154600583015460038401549395506107dc93600160a060020a039093169291029061105e565b50600060058301556107ed83611151565b6040805184815290517fb5dc9baf0cb4e7e4759fa12eadebddf9316e26147d5a9ae150c4228d5a1dd23f9181900360200190a161082933611244565b5b5b505050565b600154600160a060020a031681565b600054600160a060020a0363010000009091048116903316811461086257610000565b600080546040516301000000909104600160a060020a0316916108fc851502918591818181858888f1935050505015156103ab57610000565b5b5b5050565b60025481565b600054600160a060020a036301000000909104811690331681146108ca57610000565b6000805460408051602090810184905281517fa9059cbb0000000000000000000000000000000000000000000000000000000081526301000000909304600160a060020a0390811660048501526024840187905291519187169363a9059cbb9360448082019492918390030190829087803b156100005760325a03f115610000575050505b5b505050565b610100604051908101604052806000600160a060020a03168152602001600081526020016000815260200160008152602001600081526020016000815260200160008152602001600081525060006007600085815260200190815260200160002061010060405190810160405290816000820160009054906101000a9004600160a060020a0316600160a060020a0316600160a060020a0316815260200160018201548152602001600282015481526020016003820154815260200160048201548152602001600582015481526020016006820154815260200160078201548152505091508260001415610a4857610000565b8160400151838115610000570615610a5f57610000565b6002548410610a6d57610000565b8160400151838115610000570490508160a00151811115610a8d57610000565b610a9c8584846020015161128e565b1515610aa757610000565b60a082018051829003815260008581526007602081815260409283902086518154600160a060020a031916600160a060020a038216178255918701516001820181905593870151600282015560608701516003820155608087015160048201559351600585015560c0860151600685015560e08601519390910192909255610b319190859061105e565b1515610b3c57610000565b610b518582846080015102846060015161105e565b1515610b5c57610000565b60a0820151158015610b71575060c082015115155b15610b7f57610b7f84611151565b5b6040805185815290517fb5dc9baf0cb4e7e4759fa12eadebddf9316e26147d5a9ae150c4228d5a1dd23f9181900360200190a1610bbc85611244565b5b5050505050565b831515610bd057610000565b82851415610bdd57610000565b801580610be8575081155b15610bf257610000565b80848115610000570615610c0557610000565b6005546040805160006020918201819052825160e260020a631d010437028152600160a060020a038b8116600483015293518695949094169363740410dc9360248084019491938390030190829087803b156100005760325a03f11561000057505050604051805190501015610c7a57610000565b610c8586858761128e565b1515610c9057610000565b600554604080517fbe0140a6000000000000000000000000000000000000000000000000000000008152600160a060020a03898116600483015260006024830181905260448301869052925193169263be0140a69260648084019391929182900301818387803b156100005760325a03f115610000575050506101006040519081016040528087600160a060020a03168152602001848152602001838152602001868152602001828681156100005704815260200182815260200160068054905081526020014281525060076000600254815260200190815260200160002060008201518160000160006101000a815481600160a060020a030219169083600160a060020a031602179055506020820151816001015560408201518160020155606082015181600301556080820151816004015560a0820151816005015560c0820151816006015560e0820151816007015590505060068054806001018281815481835581811511610e2757600083815260209020610e279181019083015b80821115610e235760008155600101610e0f565b5090565b5b505050916000526020600020900160005b50600280549182905560018201905560408051918252517fb5dc9baf0cb4e7e4759fa12eadebddf9316e26147d5a9ae150c4228d5a1dd23f92509081900360200190a1610e8586611244565b5b505050505050565b600354818115610000570615610ea357610000565b600160009054906101000a9004600160a060020a0316600160a060020a031663cf35bdd060016000604051602001526040518263ffffffff1660e060020a02815260040180828152602001915050602060405180830381600087803b156100005760325a03f115610000575050604080518051600080546020938401829052845160e060020a6323b872dd028152600160a060020a038981166004830152630100000090920482166024820152604481018890529451921694506323b872dd936064808201949392918390030190829087803b156100005760325a03f1156100005750506040515115159050610f9857610000565b600554600354600160a060020a039091169063be0140a6908490600190858115610000576040805160e060020a63ffffffff8816028152600160a060020a039095166004860152921515602485015204604483015251606480830192600092919082900301818387803b156100005760325a03f1156100005750505061101d82611244565b60408051600160a060020a038416815290517f30a29a0aa75376a69254bb98dbd11db423b7e8c3473fb5bf0fcba60bcbc42c4b9181900360200190a15b5050565b600081151561106c57610000565b6001546040805160006020918201819052825160e460020a630cf35bdd028152600481018790529251600160a060020a039094169363cf35bdd09360248082019493918390030190829087803b156100005760325a03f1156100005750505060405180519050600160a060020a031663a9059cbb85856000604051602001526040518363ffffffff1660e060020a0281526004018083600160a060020a0316600160a060020a0316815260200182815260200192505050602060405180830381600087803b156100005760325a03f115610000575050604051519150505b9392505050565b6000818152600760205260409020600690810154815490919060001981019081101561000057906000526020600020900160005b5054600682815481101561000057906000526020600020900160005b50556006805460001981018083559091908280158290116111e7576000838152602090206111e79181019083015b80821115610e235760008155600101610e0f565b5090565b5b50506006548314915061122d9050578060076000600684815481101561000057906000526020600020900160005b505481526020810191909152604001600020600601555b6000828152600760205260408120600601555b5050565b60045481600160a060020a031631101561128957600454604051600160a060020a0383169180156108fc02916000818181858888f19350505050151561128957610000565b5b5b50565b600081151561129c57610000565b6001546040805160006020918201819052825160e460020a630cf35bdd028152600481018790529251600160a060020a039094169363cf35bdd09360248082019493918390030190829087803b156100005760325a03f11561000057505060408051805160006020928301819052835160e060020a6323b872dd028152600160a060020a038a811660048301523081166024830152604482018a905294519490921694506323b872dd93606480840194939192918390030190829087803b156100005760325a03f115610000575050604051519150505b93925050505600a165627a7a723058204dee0e1bf170a9d122508f3e876c4a84893b12a7345591521af4ca737bb765000029"
        disassembly = Disassembly(code)
        self.assertEqual(len(disassembly.instruction_list), 3523)

    def test_easm_from_solidity_files(self):
        for input_file in TESTDATA_INPUTS.iterdir():
            output_expected = TESTDATA_OUTPUTS_EXPECTED / (input_file.name + ".easm")
            output_current = TESTDATA_OUTPUTS_CURRENT / (input_file.name + ".easm")

            code = _compile_to_code(input_file)
            disassembly = Disassembly(code)

            output_current.write_text(disassembly.get_easm())

            self.assertEqual(output_expected.read_text(), output_current.read_text(), compare_files_error_message(output_expected, output_current))
