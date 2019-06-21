store = {}
store['args']={'num_inference_samples': 10, 'available_sample_k': 10, 'seed': 424817, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.multibald', 'experiment_description': 'RMNIST with noise k10 b5 and b10 (and k100 b10), BALD, BatchBALD and heuristic', 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 3072, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 5056, 'target_accuracy': 0.95, 'target_num_acquired_samples': 300, 'initial_percentage': 100, 'reduce_percentage': 0, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'dataset': 'DatasetEnum.repeated_mnist_w_noise', 'experiment_task_id': 'rmnist_w_noise_multibald_bald_k10_b10_424817', 'experiments_laaos': './experiment_configs/rmnist_w_noise/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=rmnist_w_noise_multibald_bald_k10_b10_424817', '--experiments_laaos=./experiment_configs/rmnist_w_noise/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6345, 'nll': 2.6272445869630574}, 'chosen_samples': [58464, 84657, 133762, 32509, 72672, 102873, 64607, 32579, 33513, 178263], 'chosen_samples_score': [1.1610111614591807, 1.8102907755505644, 2.1062803752557735, 2.2219972673004023, 2.2694495513569937, 2.298293875920916, 2.2913742713692, 2.2874146117365424, 2.3226115394984923, 2.317516329717889], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.99946762699983, 'batch_acquisition_elapsed_time': 78.11845706099939})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7013, 'nll': 1.770223865953684}, 'chosen_samples': [57625, 131460, 126612, 77898, 41354, 150883, 35429, 114470, 73363, 132080], 'chosen_samples_score': [1.274270335482805, 1.9075536880658315, 2.1841560886989417, 2.259623772251908, 2.2850375365727666, 2.302746084030674, 2.318276540380871, 2.291995431841017, 2.291094043049447, 2.2911422364723535], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.051207697999416, 'batch_acquisition_elapsed_time': 76.74409414699949})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7928, 'nll': 1.164688596290946}, 'chosen_samples': [176036, 128122, 118168, 94746, 104882, 166887, 152487, 178860, 58168, 150325], 'chosen_samples_score': [1.1619028386024883, 1.7541815394011517, 2.036157347689721, 2.1660667466641153, 2.240388190345339, 2.2931053256806617, 2.2817614470468675, 2.306605682398099, 2.281553134833467, 2.289904406815066], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.637864648999312, 'batch_acquisition_elapsed_time': 75.94036647099983})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.8216, 'nll': 0.9467921752154825}, 'chosen_samples': [35351, 151650, 72186, 116992, 170320, 174099, 109285, 153046, 99473, 54350], 'chosen_samples_score': [0.9739085178229946, 1.5990285068541774, 1.9257801276717381, 2.099869446628791, 2.191299602324948, 2.2603852627331458, 2.2276180813726043, 2.3120735684396996, 2.257940731859688, 2.2899239453473363], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.720488138000292, 'batch_acquisition_elapsed_time': 75.69255306899959})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.8308, 'nll': 0.8980661306250095}, 'chosen_samples': [81395, 9154, 162886, 151847, 154563, 135257, 34200, 81254, 7168, 85301], 'chosen_samples_score': [0.9849057496050314, 1.5581278419421234, 1.895366255418776, 2.097800871489807, 2.1930635525087268, 2.25080028936026, 2.2807789973873236, 2.3134147457052956, 2.2897039282349487, 2.294878478612355], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.559858202999749, 'batch_acquisition_elapsed_time': 76.30438760400011})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8612, 'nll': 0.8629517560052871}, 'chosen_samples': [1563, 45180, 114074, 160711, 41900, 89472, 51653, 112747, 167787, 100711], 'chosen_samples_score': [1.0306632922304597, 1.6914722660554566, 2.041518188644563, 2.1914206902678117, 2.2557527921358744, 2.27489102462318, 2.321365103544293, 2.3934252295494662, 2.284935173247594, 2.3064594050912914], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.862120325000433, 'batch_acquisition_elapsed_time': 75.70279345400013})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.8063, 'nll': 0.9157145322537422}, 'chosen_samples': [132223, 8978, 145137, 161719, 72223, 55862, 170370, 109593, 162368, 115556], 'chosen_samples_score': [0.9022547608735236, 1.4206677912317436, 1.7408587269746048, 1.9395223561277923, 2.0669752331878826, 2.117001511892587, 2.212704743113571, 2.242505262920032, 2.2515394214269815, 2.310203562526759], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.92770784000004, 'batch_acquisition_elapsed_time': 76.99077020200002})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8732, 'nll': 0.7762610718226434}, 'chosen_samples': [39818, 15191, 139855, 94902, 63791, 39673, 7438, 72903, 113076, 60517], 'chosen_samples_score': [1.0564079479902748, 1.713629624144593, 2.03628238310492, 2.192003563313571, 2.2555858982550325, 2.288681687153451, 2.292314218996329, 2.320949448930659, 2.291464655571798, 2.2906822603146972], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.24523772000066, 'batch_acquisition_elapsed_time': 78.17895436100025})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8835, 'nll': 0.7840108825659752}, 'chosen_samples': [42774, 69778, 132934, 97383, 156126, 138042, 130210, 28848, 127909, 149659], 'chosen_samples_score': [1.1326375912073117, 1.8246375565300599, 2.123103263911909, 2.242813741246065, 2.2784056877978744, 2.3124528641018403, 2.297308898129953, 2.3086845185484366, 2.3075139353144962, 2.264014338513726], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.33362536200002, 'batch_acquisition_elapsed_time': 76.61881078199985})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8847, 'nll': 0.7089401890504361}, 'chosen_samples': [37984, 164149, 123012, 140868, 118394, 160547, 127833, 121846, 274, 166242], 'chosen_samples_score': [1.1569768918170982, 1.8750020275317187, 2.146090172812876, 2.245480535277517, 2.28417104068384, 2.2863646382829126, 2.2805643314878132, 2.2942894284362483, 2.2937256044185363, 2.3277640458112785], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.614855806000378, 'batch_acquisition_elapsed_time': 76.6106971270001})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8786, 'nll': 0.7009251256215572}, 'chosen_samples': [82169, 109624, 82741, 105840, 16994, 72497, 101612, 105749, 152519, 64483], 'chosen_samples_score': [1.1836887188470255, 1.9522099861750786, 2.244773829292486, 2.2868450373742633, 2.2973218695796827, 2.312877753901003, 2.283963499793956, 2.269378057580065, 2.3091888861567, 2.2821025062934113], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.389104758999565, 'batch_acquisition_elapsed_time': 75.47632083900044})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9046, 'nll': 0.621059224779606}, 'chosen_samples': [22023, 10244, 170907, 14722, 87427, 99453, 103519, 72708, 71711, 145960], 'chosen_samples_score': [1.0854596845499742, 1.753388942715679, 2.1173823042069584, 2.2347938713286486, 2.2745376812706453, 2.293922069261536, 2.300179725304335, 2.297160232979383, 2.3031933959286826, 2.3056236109124972], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.766061892000835, 'batch_acquisition_elapsed_time': 76.96711733800021})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9184, 'nll': 0.5938347129559516}, 'chosen_samples': [22167, 11904, 75280, 160766, 142167, 144223, 1377, 52247, 64767, 13582], 'chosen_samples_score': [1.2572861627850167, 2.003947120669575, 2.2428085045385853, 2.2871811999381646, 2.2981410728572915, 2.300807989409516, 2.3354573590734287, 2.298847942534436, 2.3090721064515654, 2.3089518141942014], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.732493067999712, 'batch_acquisition_elapsed_time': 76.61943084799987})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.92, 'nll': 0.577323232706189}, 'chosen_samples': [107661, 162359, 158389, 84363, 166878, 97413, 155747, 170916, 17684, 117392], 'chosen_samples_score': [1.2846091501207932, 1.952615608267033, 2.227325545098273, 2.2789831401588447, 2.29519673547411, 2.3115068927078553, 2.3359434698981536, 2.3271606045926743, 2.354099907229426, 2.3218670299790065], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.861276863000057, 'batch_acquisition_elapsed_time': 75.92659149800056})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9138, 'nll': 0.5289065414190294}, 'chosen_samples': [143746, 94899, 114932, 140476, 94660, 120340, 175312, 146412, 52149, 144497], 'chosen_samples_score': [1.1212714940137751, 1.874380937939703, 2.107980969558964, 2.230630605529297, 2.2759120701486864, 2.310476412643652, 2.286743245044347, 2.3308796345322578, 2.2752024341570465, 2.276744688458538], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.213960618999408, 'batch_acquisition_elapsed_time': 78.59534503399937})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9229, 'nll': 0.50689362924397}, 'chosen_samples': [167132, 38698, 128954, 170782, 152427, 157373, 104172, 148512, 80869, 43618], 'chosen_samples_score': [1.0726840056803666, 1.7308267466362095, 2.0436525963326986, 2.2087512886393785, 2.262633008204638, 2.313503937774118, 2.30626378786825, 2.2981781278045417, 2.300980060347241, 2.2745140185338446], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.34576451399971, 'batch_acquisition_elapsed_time': 75.36044480000055})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9322, 'nll': 0.46614116706848147}, 'chosen_samples': [149891, 130256, 137265, 92112, 114928, 146072, 23140, 177308, 168507, 176893], 'chosen_samples_score': [1.0551861830600966, 1.6581437046474654, 2.0297436639234245, 2.18520694245041, 2.2510453613311947, 2.261832909687107, 2.278716568032652, 2.2950430422096955, 2.3237944056122286, 2.251944634711643], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.021584805000202, 'batch_acquisition_elapsed_time': 75.79866146999939})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9248, 'nll': 0.5028408099329472}, 'chosen_samples': [25186, 55648, 93222, 83962, 108512, 140050, 139781, 49517, 12063, 64636], 'chosen_samples_score': [1.0681520105823874, 1.7847413395340321, 2.0806487460662084, 2.217650898754203, 2.2719141380890906, 2.273687053452933, 2.2810259329110867, 2.310031397058479, 2.2880336837491253, 2.3191265801836423], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.312516840999706, 'batch_acquisition_elapsed_time': 77.49746505500025})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9377, 'nll': 0.46481198454737677}, 'chosen_samples': [177507, 145624, 131569, 65842, 9481, 58660, 78514, 84278, 165887, 167631], 'chosen_samples_score': [1.1691059979461862, 1.933056844255081, 2.2037807406547607, 2.267945919868645, 2.2913488833042615, 2.3078798097866824, 2.3198578146708053, 2.2845010143235025, 2.294810595712577, 2.2987274217345712], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.569033980000313, 'batch_acquisition_elapsed_time': 77.39176464999946})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9375, 'nll': 0.48497097816109663}, 'chosen_samples': [111298, 94520, 118064, 163510, 160599, 142561, 125013, 93162, 35142, 169354], 'chosen_samples_score': [1.2455167784605354, 1.9868904250313513, 2.1934023356069243, 2.2642557479211245, 2.2894873701760012, 2.2799857215507973, 2.30478277015695, 2.3097562719179194, 2.2664305185865286, 2.3318829519236877], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 26.107454985000004, 'batch_acquisition_elapsed_time': 78.36609830900034})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9317, 'nll': 0.4831694153773784}, 'chosen_samples': [164202, 149530, 52514, 106412, 103544, 134791, 143463, 96704, 172838, 162472], 'chosen_samples_score': [1.1198029511795817, 1.7910587199255454, 2.1081232786875717, 2.233215227706736, 2.2807241659886626, 2.2927372240867, 2.321969664885977, 2.272979381152115, 2.325933129120308, 2.305368317668112], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.397739178999473, 'batch_acquisition_elapsed_time': 75.1450609579988})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9314, 'nll': 0.45174019513607017}, 'chosen_samples': [52478, 99336, 172115, 94916, 46368, 52140, 172971, 149132, 49890, 72181], 'chosen_samples_score': [0.8695697028547206, 1.4726564007790177, 1.8488218161133785, 2.067794632784209, 2.1887614318693918, 2.2392575092722358, 2.2751824859548293, 2.2814895461831988, 2.2826502771557795, 2.31490899575597], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.217917796999245, 'batch_acquisition_elapsed_time': 76.86132427099983})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9304, 'nll': 0.46301049679040907}, 'chosen_samples': [125684, 110078, 103702, 45048, 83112, 33358, 143028, 27559, 12702, 20183], 'chosen_samples_score': [0.9916582443416901, 1.7294756830051445, 2.0458626566182327, 2.1868120413334604, 2.249153102578071, 2.271333407570114, 2.3007410591311874, 2.323564291481321, 2.3106613145633403, 2.2836437933485954], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.50073096000051, 'batch_acquisition_elapsed_time': 75.77242310600013})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9411, 'nll': 0.41512881705284116}, 'chosen_samples': [16286, 67886, 119757, 169200, 152352, 136286, 158520, 98627, 109200, 59834], 'chosen_samples_score': [1.1428690338161482, 1.825814002304293, 2.095566022404727, 2.211470742097762, 2.267384916257467, 2.2817120228225782, 2.2948367617713332, 2.282895164285173, 2.306105920753309, 2.2708000323540602], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.54959687200062, 'batch_acquisition_elapsed_time': 77.56974993499898})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9486, 'nll': 0.37343263192296033}, 'chosen_samples': [154829, 17296, 53976, 64295, 172086, 50414, 38408, 1075, 67316, 113181], 'chosen_samples_score': [1.139804458323029, 1.8592581362516192, 2.170770437277265, 2.26653809678864, 2.291783291549958, 2.306858195083697, 2.31457204295092, 2.318627370523323, 2.286587014485333, 2.274632585436793], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.43950244699954, 'batch_acquisition_elapsed_time': 77.6382026350002})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.937, 'nll': 0.4609720063567161}, 'chosen_samples': [132061, 118832, 45944, 47886, 62137, 177728, 7984, 72061, 100208, 143016], 'chosen_samples_score': [1.1641600901808813, 1.851282350520899, 2.1307707707452703, 2.2395360137886744, 2.2813902641368102, 2.279880977727246, 2.318038075631053, 2.3259358770825243, 2.28451476069265, 2.276048841788076], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.89667855300104, 'batch_acquisition_elapsed_time': 77.35757039099917})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9438, 'nll': 0.42584735197275875}, 'chosen_samples': [133969, 74706, 73062, 129118, 8761, 26405, 138473, 125305, 32513, 101933], 'chosen_samples_score': [1.2123413708161928, 1.895912586341726, 2.187657277740293, 2.267056360768872, 2.292780521313496, 2.28203885961287, 2.321159835514681, 2.2769496258249475, 2.2931508832249943, 2.288105565308147], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 29.36862042299981, 'batch_acquisition_elapsed_time': 76.74555603699991})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9476, 'nll': 0.42284248101055616}, 'chosen_samples': [143490, 28491, 32776, 79244, 95326, 134690, 83812, 95401, 68543, 43745], 'chosen_samples_score': [1.1567851191241603, 1.8986914227876037, 2.1561452764628544, 2.2505470524698157, 2.2849567667789543, 2.3008847138123434, 2.3221807869196045, 2.3029638544025266, 2.3083187128625315, 2.328802850696105], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.73147033299938, 'batch_acquisition_elapsed_time': 78.56695188400045})
