store = {}
store['args']={'num_inference_samples': 100, 'available_sample_k': 10, 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'seed': 1038804, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.independent', 'experiment_description': 'Reproduce b1, 5, 10 k10, 100 and default initial samples, no initial samples for all methods with BALD. (No culling!)', 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 1024, 'early_stopping_patience': 3, 'epochs': 30, 'epoch_samples': 5056, 'target_accuracy': 0.96, 'target_num_acquired_samples': 300, 'log_interval': 20, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 20, 'dataset': 'DatasetEnum.mnist', 'experiment_task_id': 'mnist_independent_bald_k100_b10_1038804', 'experiments_laaos': './experiment_configs/big_repro_b10_k100/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'initial_percentage': 100, 'reduce_percentage': 0}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=mnist_independent_bald_k100_b10_1038804', '--experiments_laaos=./experiment_configs/big_repro_b10_k100/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6663, 'nll': 2.412520448580027}, 'chosen_samples': [2916, 56564, 10386, 20183, 9508, 53000, 24311, 40685, 9154, 24960], 'chosen_samples_score': [1.18897213317197, 1.1860053360492444, 1.182188875676092, 1.1690915755465885, 1.1666329305971255, 1.1576451442903464, 1.154163936938727, 1.1538409791009265, 1.1501779383920658, 1.1477299731628974], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.352908578002825, 'batch_acquisition_elapsed_time': 66.20283912799641})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7472, 'nll': 1.5180055673977138}, 'chosen_samples': [44101, 54709, 35870, 28412, 9749, 43833, 58429, 27294, 31327, 22662], 'chosen_samples_score': [1.1355838889502636, 1.1303378788927256, 1.121880594760106, 1.116178116577161, 1.0939559472882334, 1.093211351255375, 1.0798050825527192, 1.0701552554687925, 1.0682080202130901, 1.0607868499608588], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.846267431996239, 'batch_acquisition_elapsed_time': 65.31230977299856})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7794, 'nll': 1.272505843864799}, 'chosen_samples': [27930, 11708, 11096, 41907, 47781, 51201, 33055, 7881, 2986, 11025], 'chosen_samples_score': [1.011248127487928, 0.9773882302612218, 0.9559384308353578, 0.9554884960401169, 0.9554560654411174, 0.9540392317897333, 0.9529375576457142, 0.9523817236791404, 0.951615401895471, 0.9511305442890962], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.150793689004786, 'batch_acquisition_elapsed_time': 65.43236599899683})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.8071, 'nll': 1.0948037836340665}, 'chosen_samples': [3066, 3526, 14068, 7570, 25315, 10210, 5728, 16860, 26681, 12792], 'chosen_samples_score': [1.0870423349095326, 1.065041096099825, 1.0184256421612243, 1.0131809170703696, 1.001517325874992, 0.9975958310640085, 0.9936499310459124, 0.9826637410157814, 0.9808592427980781, 0.9806382022773239], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.890086708997842, 'batch_acquisition_elapsed_time': 65.86977480500354})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7846, 'nll': 1.1450010717313883}, 'chosen_samples': [12196, 51284, 48566, 22195, 26518, 52358, 9631, 27234, 53532, 20129], 'chosen_samples_score': [0.8875509642906758, 0.8855765917424396, 0.8810777324820652, 0.8695423717863457, 0.864144225498874, 0.861137533815677, 0.8609399276803649, 0.8581622096806124, 0.8580924161609877, 0.8577585525809599], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.957612913996854, 'batch_acquisition_elapsed_time': 65.94798630900186})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.803, 'nll': 1.197889122297287}, 'chosen_samples': [52740, 32013, 23877, 57441, 57311, 5170, 2737, 56563, 44706, 2856], 'chosen_samples_score': [1.06424049724638, 1.059007407380522, 1.0582062218177994, 1.050179483304217, 1.043036972960358, 1.0429000719407653, 1.0351142724192552, 1.0348591506353686, 1.0224416025123757, 1.0124083259117187], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.775354261997563, 'batch_acquisition_elapsed_time': 65.03475736200198})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8315, 'nll': 1.0066651446403265}, 'chosen_samples': [33776, 9468, 14705, 21890, 19935, 11133, 26608, 56709, 31430, 12655], 'chosen_samples_score': [1.0182322122060656, 0.9920764935840576, 0.9874504616621601, 0.9777591889411871, 0.9777549249048683, 0.9735212136331713, 0.9703368248401856, 0.9618413436542045, 0.9611665583960368, 0.9552346677954641], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.915917867001554, 'batch_acquisition_elapsed_time': 65.59775142800208})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8738, 'nll': 0.9166829791707992}, 'chosen_samples': [59726, 11721, 483, 16959, 8447, 34304, 49607, 278, 9180, 59747], 'chosen_samples_score': [1.137034177564889, 1.1359146432420966, 1.120696399185213, 1.119052454792688, 1.111972127865034, 1.1065426574418993, 1.1055081449095594, 1.103567330962662, 1.099965370808727, 1.0942282596763615], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.69119899699581, 'batch_acquisition_elapsed_time': 65.18476052799815})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8429, 'nll': 1.0211876179380415}, 'chosen_samples': [52971, 8702, 606, 4083, 45602, 47220, 6289, 5316, 27884, 26072], 'chosen_samples_score': [1.1632361546144256, 1.1183559236528915, 1.0996460513287905, 1.0758905180238496, 1.0735264939645246, 1.073396012692726, 1.0720009057491544, 1.0692755232585003, 1.0674962268935664, 1.0628218507955434], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.57040739399963, 'batch_acquisition_elapsed_time': 65.37578508699517})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8739, 'nll': 0.7282790331797003}, 'chosen_samples': [26477, 34495, 21040, 38256, 57506, 2292, 24732, 10802, 36884, 1724], 'chosen_samples_score': [0.9407299205099603, 0.939543316488039, 0.9377175700229029, 0.9349099584921402, 0.9300690556171232, 0.9291851213251033, 0.9251531303341192, 0.9078174514855804, 0.9046480639829568, 0.9027767419072088], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.033756798002287, 'batch_acquisition_elapsed_time': 64.22544862899667})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8885, 'nll': 0.6784674722681044}, 'chosen_samples': [42199, 20832, 37974, 21642, 1812, 36704, 34122, 32421, 51819, 4061], 'chosen_samples_score': [0.9542641615780489, 0.9482139756290455, 0.9260172518321941, 0.9217661833759248, 0.9106622500303405, 0.9093270726453538, 0.9091578338022493, 0.9079271041063204, 0.8972465780698011, 0.8966315528710532], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.020947596996848, 'batch_acquisition_elapsed_time': 63.8371782549948})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9134, 'nll': 0.6282537423678043}, 'chosen_samples': [26034, 27356, 38389, 12305, 27317, 23968, 36783, 8532, 31650, 11696], 'chosen_samples_score': [1.0966821728003353, 1.0651586353407105, 1.022718193670198, 1.0096794532083504, 1.0087329426966036, 1.0048220413975817, 1.00063609355208, 1.000507023619074, 1.0003184428827296, 0.9970567739221061], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.083882922001067, 'batch_acquisition_elapsed_time': 64.1995228300002})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9056, 'nll': 0.6051215080756545}, 'chosen_samples': [37373, 15679, 35401, 33593, 55128, 20784, 5315, 43176, 20820, 19612], 'chosen_samples_score': [1.052186327784089, 1.0083814905375337, 1.0034770711200167, 1.0016988010248682, 0.9769818795191508, 0.9569870611581799, 0.9495772728037123, 0.9374650912791324, 0.9367464210840397, 0.9269653193141653], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.799538412997208, 'batch_acquisition_elapsed_time': 64.47539074700035})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9154, 'nll': 0.5821494144920111}, 'chosen_samples': [33505, 52169, 45616, 47914, 42515, 52306, 1423, 3765, 5129, 8093], 'chosen_samples_score': [1.0099678711652944, 1.0031068066924715, 0.9982250561363765, 0.9787203106495368, 0.9729988037016983, 0.9508625068182701, 0.9449514880914882, 0.9167856743635452, 0.9126065529995202, 0.9102231739761215], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.63666968200414, 'batch_acquisition_elapsed_time': 64.25117326799955})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9174, 'nll': 0.5780820110412836}, 'chosen_samples': [19942, 22272, 49658, 24608, 19868, 19590, 10044, 100, 53872, 38920], 'chosen_samples_score': [1.111421475104752, 1.062211887792872, 1.0514206848216876, 1.0429522211302267, 1.017216326384031, 1.0139952193748702, 1.0076465654132511, 0.9891146309557212, 0.9883037831568087, 0.9869167257452917], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.411934344003384, 'batch_acquisition_elapsed_time': 64.83605412600446})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9189, 'nll': 0.5846593026686309}, 'chosen_samples': [26266, 20206, 7438, 20322, 23140, 52686, 17855, 18473, 46412, 12984], 'chosen_samples_score': [0.9795790982937309, 0.9785275606657198, 0.9755802527204298, 0.9743702667856913, 0.973322843909193, 0.9396986297615423, 0.9371099729492415, 0.9361554046945016, 0.9289511039736779, 0.9273913569445018], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.39628153800004, 'batch_acquisition_elapsed_time': 64.43146430599882})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9201, 'nll': 0.6233895753751992}, 'chosen_samples': [42703, 8715, 20855, 31883, 32277, 424, 42317, 16102, 49517, 3810], 'chosen_samples_score': [1.2117917417014241, 1.1470239158876612, 1.0944619069636086, 1.093117747288813, 1.0819527791119001, 1.0658714335350807, 1.0556704815280669, 1.0546448709533178, 1.0543153062328146, 1.0504171543040899], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.906472875001782, 'batch_acquisition_elapsed_time': 64.24434246199962})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9302, 'nll': 0.49418277694398177}, 'chosen_samples': [24533, 5684, 1674, 43278, 56244, 828, 44998, 22083, 44952, 2034], 'chosen_samples_score': [0.9688052941398779, 0.9650089708903187, 0.93784257329794, 0.9325864972878827, 0.9275176256885284, 0.9244928828969367, 0.9119212605864062, 0.9113369450765215, 0.9003766146605584, 0.890097743440174], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.8466022529974, 'batch_acquisition_elapsed_time': 64.3632605649982})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9206, 'nll': 0.5309119568089248}, 'chosen_samples': [32880, 44898, 25538, 31014, 42746, 5175, 36460, 45732, 14878, 38524], 'chosen_samples_score': [0.9922958516193007, 0.9572599741342778, 0.9448177213832734, 0.9259075769559031, 0.9210153679246147, 0.9173006171260172, 0.9123128160314308, 0.9101895534205693, 0.905721424560157, 0.904296736555699], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.35245757499797, 'batch_acquisition_elapsed_time': 64.80253717600135})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9226, 'nll': 0.5489729117006066}, 'chosen_samples': [33338, 47076, 20037, 12066, 46616, 5548, 31184, 8780, 52228, 32776], 'chosen_samples_score': [1.0064739676673935, 0.953172808590527, 0.9455123979967613, 0.9426115241940854, 0.934083170663745, 0.9286695377349886, 0.9125781578069739, 0.9027815190913043, 0.9011495529474225, 0.8952361831388486], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.521606148999126, 'batch_acquisition_elapsed_time': 64.61581215300248})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9381, 'nll': 0.550032089975834}, 'chosen_samples': [40066, 26358, 34520, 35205, 10500, 42787, 57714, 39480, 47209, 52137], 'chosen_samples_score': [1.2462454606232836, 1.2006623274326849, 1.1398751757239352, 1.1115035636065347, 1.1071073273512702, 1.0960561838845644, 1.087461004232071, 1.0810607701692736, 1.0731554076939944, 1.0702326244645022], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.260493735993805, 'batch_acquisition_elapsed_time': 64.5465616099973})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9429, 'nll': 0.4614778189615012}, 'chosen_samples': [15973, 29294, 59286, 59294, 59565, 47587, 34819, 5332, 57728, 1642], 'chosen_samples_score': [1.0233618428517273, 0.995292190618067, 0.9847675325890753, 0.9814851146792021, 0.9698760488837095, 0.9611757503161802, 0.9609090873370685, 0.9525530541900246, 0.9492495259510643, 0.9444721816356076], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.35956139100017, 'batch_acquisition_elapsed_time': 64.41315901200142})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.945, 'nll': 0.4564485756090283}, 'chosen_samples': [42209, 49064, 43416, 54794, 42428, 28388, 59289, 15948, 37967, 16544], 'chosen_samples_score': [0.9979717984160811, 0.9926845737652245, 0.9919604484281369, 0.9878132209000341, 0.987559342925527, 0.9724388415429082, 0.9601660816797747, 0.9578669963345098, 0.9578344034706696, 0.9549019162173409], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.895506411994575, 'batch_acquisition_elapsed_time': 64.6149992760038})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9559, 'nll': 0.3781200381428003}, 'chosen_samples': [16488, 22531, 11536, 25873, 27169, 8879, 18487, 39561, 27101, 37469], 'chosen_samples_score': [1.0145410901523257, 0.9299620152906254, 0.914523862441889, 0.9048020504306847, 0.8986124013838668, 0.8949430683560422, 0.8924694726572328, 0.8924504618447844, 0.8862905111492442, 0.8692744578963661], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.026215990998026, 'batch_acquisition_elapsed_time': 64.30407159099559})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9544, 'nll': 0.3896368427545427}, 'chosen_samples': [36818, 32276, 24278, 35246, 55758, 6066, 5103, 27172, 45944, 49282], 'chosen_samples_score': [1.1031691383244837, 1.0195896527257142, 1.0008997965196311, 0.9995731517273867, 0.9947881810721051, 0.9928731465431391, 0.9804616756635228, 0.9736163422785662, 0.9695082728346626, 0.9670004190705104], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.4326522390038, 'batch_acquisition_elapsed_time': 64.17816928200045})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9485, 'nll': 0.4341083853272796}, 'chosen_samples': [52914, 52690, 1127, 31312, 6920, 18324, 35435, 33364, 5305, 340], 'chosen_samples_score': [1.040408752560279, 1.0381717740908063, 1.035027931096727, 1.0294142899540317, 1.0113028625247136, 1.0101123129846372, 1.0082464790727412, 1.0038742143924506, 1.0012952028999305, 1.0000470390033507], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.22583482700429, 'batch_acquisition_elapsed_time': 64.78456257200014})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9526, 'nll': 0.39305880080950256}, 'chosen_samples': [49242, 16756, 4646, 18598, 7984, 38698, 46368, 4153, 35102, 59681], 'chosen_samples_score': [0.9377914777850129, 0.9159510779751686, 0.9059491720680182, 0.9032085198711574, 0.9026972153672358, 0.8987360271224627, 0.8976459495001883, 0.8973930780149558, 0.8897339230430433, 0.8870568450086287], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.809731613997428, 'batch_acquisition_elapsed_time': 64.94955695599492})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.964, 'nll': 0.3563751041017176}, 'chosen_samples': [24740, 49487, 54950, 34920, 3691, 32747, 14385, 57523, 17296, 17603], 'chosen_samples_score': [1.0301501544624387, 1.025766982121087, 0.9877009813391013, 0.9848664485995794, 0.9753249749068662, 0.9719717550034591, 0.9514339081339729, 0.9490899821953825, 0.9446354101821954, 0.9416061525081079], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.424050988003728, 'batch_acquisition_elapsed_time': 65.09111662500072})
